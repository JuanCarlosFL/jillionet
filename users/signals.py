from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from .models import UserBalance
from orderbook.models import Currency


User = get_user_model()


@receiver(post_save, sender=User)
def create_user_balance(sender, instance, created, **kwargs):
    if created:
        for currency in Currency.objects.all():
            if currency.name == 'JILL':                
                UserBalance.objects.create(currency=currency, user=instance, ammount=5000)
            else:
                UserBalance.objects.create(currency=currency, user=instance)
        #UserBalance.objects.create(currency__name="ETH", user=instance)        
        #UserBalance.objects.create(currency__name="USDT", user=instance)
        #UserBalance.objects.create(currency__name="BUSD", user=instance)
        #UserBalance.objects.create(currency__name="BNB", user=instance)
        #UserBalance.objects.create(currency__name="JILL", user=instance, ammount=5000)
    
        
