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


class UserBalance(models.Model):
   currency = models.ForeignKey('orderbook.Currency', on_delete=models.SET_NULL, null=True)
   amount = models.DecimalField(decimal_places=18, max_digits=36, default=0)
   user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

   class Meta:
      unique_together = ['currency', 'user']

   