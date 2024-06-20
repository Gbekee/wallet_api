from rest_framework import serializers
from .models import User, Beneficiary, Transaction, Wallet

class WalletSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Wallet
        fields=['num', 'balance', 'pin', 'card', 'user']

class UserSerializer(serializers.ModelSerializer):
    wallet=WalletSerializer(many=True, read_only=True)
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'email', 'wallets']


class BeneficiarySerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=Beneficiary
        fields=['user','beneficiaries']

class TransactionSerializer(serializers.ModelSerializer):
    receiver=serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all, read_only=True)
    initiator=serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all,read_only=True)
    class Meta:
        model=Transaction
        fields='__all__'
    
