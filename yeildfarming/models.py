from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class yeildcontract(models.Model):
    yeildpair = models.CharField(max_length=200, unique=True)
    liquidity = models.CharField(max_length=200, unique=True)
    APR = models.CharField(max_length=200, unique=True)
    APYd365 = models.CharField(max_length=200, unique=True)
    d30 = models.CharField(max_length=200, unique=True)
    d7 = models.CharField(max_length=200, unique=True)
    d1 = models.CharField(max_length=200, unique=True)

    

    def __str__(self):
        return f"{self.code}"
