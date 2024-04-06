from django.contrib import admin
from .models import UserBankAccount, UserAddress, BankRuptModel
# Register your models here.

admin.site.register(UserBankAccount)
admin.site.register(UserAddress)
admin.site.register(BankRuptModel)