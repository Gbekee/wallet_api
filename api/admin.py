from django.contrib import admin
from .models import User, Transaction, Beneficiary, Wallet
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password', 'first_name', 'last_name', 'email', 'phone')

class WalletAdmin(admin.ModelAdmin):
    readonly_fields = ('num', 'balance', 'pin', 'card', 'user')

class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('initiator', 'amount', 'receiver', 'description', 'time')

class BeneficaryAdmin(admin.ModelAdmin):
    readonly_fields=('user', 'bank', 'beneficiaries', 'e_wallet', 'favourite')
admin.site.register(User, UserAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Beneficiary, BeneficaryAdmin)
admin.site.register(Wallet, WalletAdmin)
