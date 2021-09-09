from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class YeildContract(models.Model):
    yeildpair = models.CharField(max_length=200, unique=True)
    liquidity = models.IntegerField()
    APR = models.DecimalField(decimal_places=2, max_digits=7)
    APYd365 = models.CharField(max_length=200)
    d30 = models.CharField(max_length=200)
    d7 = models.CharField(max_length=200)
    d1 = models.CharField(max_length=200)    

    def __str__(self):
        return f"{self.yeildpair}"

    def get_first_pair(self):
        return self.yeildpair.split("-")[0]

    def get_2nd_pair(self):
        return self.yeildpair.split("-")[1]
