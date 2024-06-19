from django.db import models
from datetime import datetime
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone,password):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError('Password required')
        
        user=self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            phone=phone
        )
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, first_name, last_name, email, phone ,password):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError('Password required')
        user=self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            phone=phone,
            password=password
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser):
    first_name=models.CharField(verbose_name='First name', max_length=50)
    last_name=models.CharField(verbose_name='Last name', max_length=50)
    email=models.EmailField(unique=True)
    # password=models.CharField(max_length=255)
    address=models.TextField()
    phone=models.IntegerField(verbose_name='Phone number')
    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name', 'phone', 'password']

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, api_label):
        return True
    def add_wallet(self,*args, **kwargs):
       
        x=Wallet()
        x.num=x.generate_account()
        x.card=x.generate_card()
        x.user=self
        x.pin=make_password('0000')
        x.save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            x=Wallet()
            x.num=x.generate_account()
            x.card=x.generate_card()
            x.user=self
            x.pin=make_password('0000')
            x.save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
    
    def set_beneficiary(self, beneficiary, choice):
        beneficiary=Beneficiary()
        if choice=='favourite':
            beneficiary.favourite=True
        elif choice=='bank':
            beneficiary.bank=True
        elif choice=='e_wallet':
            beneficiary.e_wallet=True
        else:
            raise ValueError('Enter valid choice')
        beneficiary.user=self
        beneficiary.beneficiary=beneficiary
        beneficiary.save()

    def __str__(self):
        return self.first_name
    
class Wallet(models.Model):
    num=models.IntegerField(verbose_name='Account number', unique=True)
    balance=models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    pin=models.CharField(max_length=255)
    card=models.IntegerField(verbose_name='Card number', unique=True)
    user=models.ForeignKey(User,  on_delete=models.CASCADE, related_name='wallets')
    
    def save(self, *args, **kwargs):
        if not self.num:
            self.num=self.generate_account(self)
        if not self.card:
            self.card=self.generate_card(self)
            self.pin=self.set_password('000')
        super().save(*args, **kwargs)

    def generate_account(self):
        while True:
            account_number=''.join(str(random.randint(0,9)) for i in range(10))
            account_number=int(account_number)
            if not Wallet.objects.filter(num=account_number).exists():
                return account_number
    def generate_card(self):
        while True:
            card_number=''.join(str(random.randint(0,9)) for i in range(16))
            card_number=int(card_number)
            if not Wallet.objects.filter(card=card_number).exists():
                return card_number


    def send_money(self, receiver, amount, description=None):
        if int(self.balance)<amount:
            return ValueError('Insufficient balance')
             
        self.balance-=amount
        self.save()

        receiver.balance+=amount
        receiver.save()

        description=description
        transaction=Transaction()
        transaction.initiator=self
        transaction.reciever=receiver
        transaction.description=description
        transaction.amount=amount
        transaction.save()

        # beneficiary, created=Beneficiary.objects.get_or_create(user=self.user, beneficiaries=receiver)
        if not Beneficiary.objects.filter(user=self.user).exists():
            beneficiary=Beneficiary(user=self.user)
            beneficiary.save()
            beneficiary.beneficiaries.add(receiver.id)
        elif not Beneficiary.objects.filter(user=self.user, beneficiaries=receiver).exists():
            Beneficiary.objects.get(user=self.user).beneficiaries.add(receiver.id)
        
            
            

    
        return transaction
    
    def __str__(self):
        return f'{self.user} wallet: {self.id}'
    
class Beneficiary(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    beneficiaries = models.ManyToManyField(Wallet, related_name='beneficiaries')
    favourite = models.BooleanField(default=False)
    bank = models.BooleanField(default=False)
    e_wallet = models.BooleanField(default=False)


class Transaction(models.Model):
    initiator=models.ForeignKey(Wallet, on_delete=models.PROTECT)
    amount=models.DecimalField(max_digits=20, decimal_places=3)
    reciever=models.ForeignKey(Wallet, related_name='transactions', on_delete=models.PROTECT)
    description=models.CharField(max_length=100)
    time=models.DateTimeField('Time initiated', auto_now_add=True, blank=True)