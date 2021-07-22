from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
   phone_number = PhoneNumberField(unique=True)
