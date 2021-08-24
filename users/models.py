from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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
    user_level = models.CharField(max_length=50, choices=USER_LEVEL_CHOICES, default=BRONZE)
    # balance = models.ForeignKey("UserBalance", on_delete=models.SET_NULL, null=True, blank=True)


class BalanceFor(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class UserBalance(models.Model):
    currency = models.ForeignKey('orderbook.Currency', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(decimal_places=18, max_digits=36, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    public_key = models.TextField(null=True, blank=True)
    balance_for = models.ForeignKey(BalanceFor, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ['currency', 'user', 'balance_for']
        ordering = ['user', 'currency__code']


class User_level_field(models.Model):
    level_key = models.CharField(max_length=200, unique=True)
    borrow_interest = models.CharField(max_length=200, unique=True)
    maker_taker = models.CharField(max_length=200, unique=True)
    inicial_balance_USDT = models.CharField(max_length=200, unique=True)
    free_balance_JILL = models.CharField(max_length=200, unique=True)
    max_withdraw_USDT = models.CharField(max_length=200, unique=True)
    Jillion_hold_trigger = models.CharField(max_length=200, unique=True)
    Futures_leverage = models.CharField(max_length=200, unique=True)
