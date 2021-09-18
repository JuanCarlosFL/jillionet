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
    required_level = models.ForeignKey('users.UserLevel', on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return f"{self.yeildpair}"

    def get_first_pair(self):
        return self.yeildpair.split("-")[0]

    def get_2nd_pair(self):
        return self.yeildpair.split("-")[1]


class YeildOrderBook(models.Model):

    KLINE_INTERVAL_3DAY = '3d'
    KLINE_INTERVAL_1WEEK = '1w'
    KLINE_INTERVAL_1MONTH = '1m'
    KLINE_INTERVAL_3MONTH = '3m'
    KLINE_INTERVAL_6MONTH = '6m'
    KLINE_INTERVAL_1YEAR = '1y'
    KLINE_INTERVAL_2YEAR = '2y'
    KLINE_INTERVAL_3YEAR = '3y'

    TIMEFRAME_CHOICES = (
        (KLINE_INTERVAL_3DAY, KLINE_INTERVAL_3DAY),
        (KLINE_INTERVAL_1WEEK, KLINE_INTERVAL_1WEEK),
        (KLINE_INTERVAL_1MONTH, KLINE_INTERVAL_1MONTH),
        (KLINE_INTERVAL_3MONTH, KLINE_INTERVAL_3MONTH),
        (KLINE_INTERVAL_6MONTH, KLINE_INTERVAL_6MONTH),
        (KLINE_INTERVAL_1YEAR, KLINE_INTERVAL_1YEAR),
        (KLINE_INTERVAL_2YEAR, KLINE_INTERVAL_2YEAR),
        (KLINE_INTERVAL_3YEAR, KLINE_INTERVAL_3YEAR),
    )

    NEW = 'new'
    ACTIVE = 'active'
    FINISH = 'finish'

    STATUS_CHOICES = (
        (NEW, NEW.title()),
        (ACTIVE, ACTIVE.title()),
        (FINISH, FINISH.title()),
    )
    
    
    #volume = models.DecimalField(decimal_places=18, max_digits=36, default=10000)
    jill_purchase_commission= models.DecimalField(decimal_places=18, max_digits=36, default=0.005)# Default value change
    Jill_reward = models.DecimalField(decimal_places=18, max_digits=36, default=10000)
    coin_reward = models.DecimalField(decimal_places=18, max_digits=36, default=10000)
    volume = models.DecimalField(decimal_places=18, max_digits=36, default=10000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default=NEW)
    contract_pair = models.ForeignKey(YeildContract, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
