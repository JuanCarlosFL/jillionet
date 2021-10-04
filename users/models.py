import json
from web3 import Web3

from django.contrib.auth.models import AbstractUser
from django.core import serializers
from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from decimal import Decimal
from django.conf import settings


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

# Create your models here.


class User(AbstractUser):
    DAIMOND = 'diamond'
    GOLD = 'gold'
    SILVER = 'silver'
    COPPER = 'copper'
    PLATINUM = 'platinum'
    BRONZE = 'bronze'

    USER_LEVEL_CHOICES = (
        (DAIMOND, DAIMOND.title()),
        (GOLD, GOLD.title()),
        (SILVER, SILVER.title()),
        (COPPER, COPPER.title()),
        (PLATINUM, PLATINUM.title()),
        (BRONZE, BRONZE.title()),
    )
    phone_number = PhoneNumberField(unique=True)
    level = models.ForeignKey('UserLevel', on_delete=models.SET_NULL, null=True, blank=True)
    jillion_public_key = models.TextField(blank=True, null=True)
    rank = models.IntegerField(null=True, blank=True)
    loan = models.OneToOneField('Loan', on_delete=models.CASCADE, null=True, blank=True)
    # user_level = models.CharField(max_length=50, choices=USER_LEVEL_CHOICES, default=BRONZE, null=True)
    # balance = models.ForeignKey("UserBalance", on_delete=models.SET_NULL, null=True, blank=True)

    def get_balance(self, bal_type):
        my_balance = self.userbalance_set.filter(user=self, balance_for__name=bal_type)
        my_balance_values = my_balance.values('id', 'balance_for__name', 'amount', 'staked', 'currency__code', 'currency__default_public_key', 'public_key')
        #print(my_balance_values)
        return my_balance_values

    def get_jill_balance(self):
        return self.get_balance('jillfarm').filter(currency__code='JILL').first()

    def get_currency_balance(self, balance_for, currency):
        return self.get_balance(balance_for).filter(currency__code=currency).first()

    def get_jill_wallet_ballance(self):
        # ABI = json.loads(ABI_json)
        w3 = Web3(Web3.HTTPProvider(settings.INFURA_KEY))
        #print(w3.isConnected())

        contract_address = '0x83053843161Ef9fe5b44211a56d2ADf201BeDEF9'

        contract = w3.eth.contract(contract_address, abi=settings.JILLION_ABI)
        holder = Web3.toChecksumAddress(self.jillion_public_key)
        raw_balance = contract.functions.balanceOf(holder).call()
        return Decimal(raw_balance)/(10**18)


class BalanceFor(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class UserBalance(models.Model):

    DEPOSIT = 'deposit'
    WITHDRAW = 'withdraw'
    TRANSFER = 'transfer'

    BALANCE_ACTION = (
        (DEPOSIT, DEPOSIT.title()),
        (WITHDRAW, WITHDRAW.title()),
        (TRANSFER, TRANSFER.title()),
    )

    currency = models.ForeignKey('orderbook.Currency', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(decimal_places=18, max_digits=36, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    public_key = models.TextField(null=True, blank=True)
    balance_for = models.ForeignKey(BalanceFor, on_delete=models.SET_NULL, null=True)
    staked = models.DecimalField(decimal_places=18, max_digits=36, default=0)
    updated_at = models.DateTimeField(default=timezone.now)
    action = models.CharField(max_length=200, choices=BALANCE_ACTION, null=True)

    class Meta:
        unique_together = ['currency', 'user', 'balance_for']
        ordering = ['user', 'currency__code']


class UserLevel(models.Model):
    level_key = models.CharField(max_length=200, unique=True)
    borrow_interest = models.CharField(max_length=200, unique=True)
    maker_taker = models.CharField(max_length=200, unique=True)
    inicial_balance_USDT = models.CharField(max_length=200, unique=True)
    free_balance_JILL = models.DecimalField(decimal_places=18, max_digits=36, default=0)
    max_withdraw_USDT = models.CharField(max_length=200, unique=True)
    Jillion_hold_trigger = models.DecimalField(decimal_places=18, max_digits=36, default=0)
    Futures_leverage = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.level_key


class Loan(models.Model):
    ACTIVE = 'active'
    PAID = 'paid'
    STATUS_CHOICES = (
        (PAID, PAID.title()),
        (ACTIVE, ACTIVE.title()),
    )

    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default=ACTIVE)
    amount = models.DecimalField(decimal_places=18, max_digits=36, default=0)

    def __str__(self):
        try:
            return f'{self.user.username}--{self.amount}--{self.status}'
        except User.DoesNotExist:
            return f'{self.amount}--{self.status}'
