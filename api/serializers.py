from rest_framework import serializers
from .models import User, Beneficiary, Transaction, Wallet

class TransactionSerializer(serializers.ModelSerializer):
    receiver=serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())
    initiator=serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())
    class Meta:
        model=Transaction
        fields='__all__'

class BeneficiarySerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    beneficiaries=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Beneficiary
        fields=['user','beneficiaries', 'favourite', 'bank', 'e_wallet']

class WalletSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    debits=TransactionSerializer(many=True)
    credits=TransactionSerializer(many=True)
    class Meta:
        model=Wallet
        fields=['num', 'balance', 'pin', 'card', 'user', 'debits', 'credits']
        extra_kwargs={
            'num':{'read_only' : True},
            'balance':{'read_only' : True},
            'card':{'read_only' : True},
            'credits':{'read_only' : True},
            'debits':{'read_only' : True},
            'pin':{'write_only' : True}
        }
        
class UserSerializer(serializers.ModelSerializer):
    wallets=WalletSerializer(many=True, read_only=True)
    name=serializers.SerializerMethodField()
    # beneficiaries=BeneficiarySerializer(many=True)
    class Meta:
        
        model=User
        fields=['first_name', 'last_name', 'email', 'wallets', 'name']
        # fields='__all__'
        extra_kwargs={
            'first_name':{'write_only' : True},
            'last_name':{'write_only' : True},
            # 'wallets': {'read_only' : True}, 
            'password':{'write_only':True}

        }

    def to_representation(self, instance):
        ret=super().to_representation(instance)
        ret['name']=ret['name'].title()
        return ret
    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'





    
