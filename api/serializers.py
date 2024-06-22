from rest_framework import serializers
from .models import User, Beneficiary, Transaction, Wallet
from rest_framework.response import Response

class TransactionSerializer(serializers.ModelSerializer):
    receiver=serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())
    initiator=serializers.PrimaryKeyRelatedField(queryset=Wallet.objects.all())
    time_initiated=serializers.SerializerMethodField()
    class Meta:
        model=Transaction
        fields=['initiator', 'receiver', 'amount', 'description', 'time_initiated']
        extra_kwargs={
            'time':{'read_only':True}
        }
    def create(self, validated_data):
        if validated_data['initiator']==validated_data['receiver'] or float(validated_data['amount'])>float(validated_data['receiver'].balance):
            print('\nInvalid\n')
            raise ValueError({ 
                    'error': ['Invalid Operation']
                })
        
        return validated_data['initiator'].send_money(validated_data['receiver'].num, validated_data['amount'], validated_data['description'])
    def get_time_initiated(self, obj):
        return obj.time.strftime('%H:%M:%S %D')

class BeneficiarySerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(read_only=True)
    beneficiaries=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model=Beneficiary
        fields=['user','beneficiaries', 'favorites', 'banks', 'e_wallets']

class WalletSerializer(serializers.ModelSerializer):
    debits=TransactionSerializer(many=True, read_only=True)
    credits=TransactionSerializer(many=True, read_only=True)
    class Meta:
        model=Wallet
        fields=['id', 'bank', 'num', 'balance', 'pin', 'card', 'user', 'credits', 'debits']
        extra_kwargs={
            'num':{'read_only' : True},
            'balance':{'read_only' : True},
            'card':{'read_only' : True},
            'credits':{'read_only' : True},
            'debits':{'read_only' : True},
            'pin':{'write_only' : True},
            'user':{'read_only' : True},
            'bank':{'read_only' : True}
        }
        
class UserSerializer(serializers.ModelSerializer):
    wallets=WalletSerializer(many=True, read_only=True)
    name=serializers.SerializerMethodField()
    # beneficiaries=BeneficiarySerializer(many=True)
    class Meta:
        
        model=User
        fields=['id','first_name', 'last_name','name', 'email', 'phone','wallets',  'password']
        extra_kwargs={
            'first_name':{'write_only' : True},
            'last_name':{'write_only' : True},
            'password':{'write_only':True}

        }

    def to_representation(self, instance):
        ret=super().to_representation(instance)
        ret['name']=ret['name'].title()
        return ret
    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'





    
