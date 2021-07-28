from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class iabotcontract(models.Model):# Analize all market 
    contractnumber = models.CharField(max_length=200, unique=True)
    pair = models.CharField(max_length=200, unique=True)
    timeframe = models.CharField(max_length=200, unique=True)
    win_close_point = models.CharField(max_length=200, unique=True)
    lose_close_point = models.CharField(max_length=200, unique=True)
 


    def __str__(self):
        return f"{self.contractnumber}"

class iabotOrderbook(models.Model): # Works only in The B Book 
    
    pair = models.CharField(max_length=200, unique=True)
    volume = models.CharField(max_length=200, unique=True)
    buy_sell = models.CharField(max_length=200, unique=True)
    loop_time_frame = models.CharField(max_length=200, unique=True)
    random_spred = models.CharField(max_length=200, unique=True)
 


    def __str__(self):
        return f"{self.contractnumber}"



