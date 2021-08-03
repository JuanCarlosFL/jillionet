from django.db import models

# Create your models here.
#class gethistoricaldatamodel(models.Model):# 

    #symbol= = models.CharField(max_length=200)  #///
    #interval= = models.CharField(max_length=200)#///
    #number_of_candel = models.CharField(max_length=200)#///
    
    #Open = models.CharField(max_length=200)
    #High = models.CharField(max_length=200)
    #Low = models.CharField(max_length=200)
    #Close = models.CharField(max_length=200)
    #Volume = models.CharField(max_length=200)
    #Closetime = models.CharField(max_length=200)
    #AsetVolume = models.CharField(max_length=200)
    #Trades = models.CharField(max_length=200)
    #TBBAV = models.CharField(max_length=200)
    #TBQAV = models.CharField(max_length=200)
    #ignore = models.CharField(max_length=200)


class Historicaldata(models.Model):
    symbol = models.CharField(max_length=200)
    data = models.JSONField()

    def __str__(self):
        return self.symbol


