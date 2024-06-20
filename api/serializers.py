from rest_framework import serializers
from .models import User, Beneficiary, Transaction, Wallet

class WalletSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model=Wallet
        fields=['num', 'balance', 'pin', 'card', 'user']
        
class UserSerializer(serializers.ModelSerializer):
    wallets=WalletSerializer(many=True, read_only=True)
    name=serializers.SerializerMethodField()
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


class BeneficiarySerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    beneficiaries=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Beneficiary
        fields=['user','beneficiaries']

class TransactionSerializer(serializers.ModelSerializer):
    receiver=serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())
    initiator=serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())
    class Meta:
        model=Transaction
        fields='__all__'
    
