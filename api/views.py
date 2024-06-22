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

class TransactionsViewSet(generics.ListCreateAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer


class WalletsViewSet(generics.ListCreateAPIView):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer

class WalletDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset=Wallet.objects.all()
    serializer_class=WalletSerializer

class TransactionDetailViewSet(generics.ListAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

class BeneficiariesViewSet(generics.ListAPIView):
    queryset=Beneficiary.objects.all()
    serializer_class=BeneficiarySerializer

class BeneficiaryDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset=Beneficiary.objects.all()
    serializer_class=BeneficiarySerializer