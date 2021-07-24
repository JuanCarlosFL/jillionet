from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Currency(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code}"


class Order(models.Model):

    MARKET = 'market'
    LIMIT = 'limit'

    ORDER_TYPE_CHOICES = (
        (MARKET, MARKET.title()),
        (LIMIT, LIMIT.title())
    )

    NEW = 'new'
    FILL = 'fill'

    STATUS_CHOICES = (
        (NEW, NEW.title()),
        (FILL, FILL.title())
    )

    SPOT = 'spot'
    FUTURES = 'futures'
    CONTRACT_TYPE_CHOICES = (
        (SPOT, SPOT.title()),
        (FUTURES, FUTURES.title())
    )

    BUY = 'buy'
    SELL = 'sell'
    BUY_SELL_CHOICES = (
        (BUY, BUY.title()),
        (SELL, SELL.title())
    )
    
    buy_sell = models.CharField(max_length=10, choices=BUY_SELL_CHOICES)
    order_type = models.CharField(max_length=200, choices=ORDER_TYPE_CHOICES, default=MARKET)
    volume = models.DecimalField(decimal_places=18, max_digits=36)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default=NEW)
    contract_type = models.CharField(max_length=200, choices=CONTRACT_TYPE_CHOICES, default=SPOT)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)



