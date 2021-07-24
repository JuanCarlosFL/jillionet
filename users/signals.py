from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from .models import UserBalance


User = get_user_model()


@receiver(post_save, sender=User)
def create_user_balance(sender, instance, created, **kwargs):
    if created:
        UserBalance.objects.create(currency_name="BTC", user=instance)
        UserBalance.objects.create(currency_name="ETH", user=instance)        
        UserBalance.objects.create(currency_name="USDT", user=instance)
        UserBalance.objects.create(currency_name="BUSD", user=instance)
        UserBalance.objects.create(currency_name="BNB", user=instance)
        UserBalance.objects.create(currency_name="JILL", user=instance, ammount=5000)
    
        
