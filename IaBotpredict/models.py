from django.db import models
from django.contrib.auth import get_user_model

from orderbook.models import Order

User = get_user_model()








class iabotcontract(models.Model):# Analize all market 
    contract_number = models.CharField(max_length=200, unique=True)
    pair = models.ForeignKey('orderbook.TradingPair', on_delete=models.CASCADE)
    timeframe = models.CharField(max_length=200, choices=Order.TIMEFRAME_CHOICES)
    win_close_point = models.CharField(max_length=200)
    lose_close_point = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.contract_number}"


class iabotOrderbook(models.Model): # Works only in The B Book 
    
    pair = models.CharField(max_length=200, unique=True)
    volume = models.CharField(max_length=200, unique=True)
    buy_sell = models.CharField(max_length=200, unique=True)
    loop_time_frame = models.CharField(max_length=200, unique=True)
    random_spred = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.pair}"



