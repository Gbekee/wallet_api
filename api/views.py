from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, TransactionSerializer, WalletSerializer, BeneficiarySerializer
from .models import User, Transaction, Wallet, Beneficiary
# Create your views here.
class UserViewSet(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer