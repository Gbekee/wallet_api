from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, TransactionSerializer, WalletSerializer, BeneficiarySerializer
from .models import User, Transaction, Wallet, Beneficiary

# Create your views here.
class UsersViewSet(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class TransactionsViewSet(generics.ListAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

class WalletsViewSet(generics.ListAPIView):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer

class WalletDetailViewSet(generics.ListAPIView):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer

class TransactionDetailViewSet(generics.ListAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

class BeneficiariesViewSet(generics.ListCreateAPIView):
    queryset=Beneficiary.objects.all()
    serializer_class=BeneficiarySerializer

class BeneficiaryDetailViewSet(generics.ListAPIView):
    queryset=Beneficiary.objects.all()
    serializer_class=BeneficiarySerializer