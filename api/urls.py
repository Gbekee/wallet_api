from django.urls import path
from . import views

urlpatterns=[
    path('api/users', views.UsersViewSet.as_view(), name='users'),
    path('api/users/<int:pk>', views.UserDetailViewSet.as_view(), name='users'),
    path('api/transactions', views.TransactionsViewSet.as_view(), name='users'),
    path('api/transactions/<int:pk>', views.TransactionDetailViewSet.as_view(), name='users'),
    path('api/wallets', views.WalletsViewSet.as_view(), name='users'),
    path('api/wallets/<int:pk>', views.WalletDetailViewSet.as_view(), name='users'),
    path('api/beneficiaries', views.BeneficiariesViewSet.as_view(), name='users'),
    path('api/benefies/<int:pk>', views.BeneficiaryDetailViewSet.as_view(), name='users')
]