from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.fields import AutoSlugField


User = get_user_model()


def my_slugify_function(content):
    return content.replace('/', '_').upper()


class TradingPair(models.Model):
    pair = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='pair', slugify_function=my_slugify_function, unique=True, null=True)

    def __str__(self):
        return f"{self.pair}"


class Currency(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=10, unique=True)
    chain = models.CharField(max_length=10, default='ERC-20')
    last_price = models.DecimalField(max_digits=32, decimal_places=18, null=True)
    contract_creator_hash = models.CharField(max_length=200, default='none')


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


    KLINE_INTERVAL_1MINUTE = '1m'
    KLINE_INTERVAL_3MINUTE = '3m'
    KLINE_INTERVAL_5MINUTE = '5m'
    KLINE_INTERVAL_15MINUTE = '15m'
    KLINE_INTERVAL_30MINUTE = '30m'
    KLINE_INTERVAL_1HOUR = '1h'
    KLINE_INTERVAL_2HOUR = '2h'
    KLINE_INTERVAL_4HOUR = '4h'
    KLINE_INTERVAL_6HOUR = '6h'
    KLINE_INTERVAL_8HOUR = '8h'
    KLINE_INTERVAL_12HOUR = '12h'
    KLINE_INTERVAL_1DAY = '1d'
    KLINE_INTERVAL_3DAY = '3d'
    KLINE_INTERVAL_1WEEK = '1w'
    KLINE_INTERVAL_1MONTH = '1M'

    TIMEFRAME_CHOICES = (
        (KLINE_INTERVAL_1MINUTE, KLINE_INTERVAL_1MINUTE),
        (KLINE_INTERVAL_3MINUTE, KLINE_INTERVAL_3MINUTE),
        (KLINE_INTERVAL_5MINUTE, KLINE_INTERVAL_5MINUTE),
        (KLINE_INTERVAL_15MINUTE, KLINE_INTERVAL_15MINUTE),
        (KLINE_INTERVAL_30MINUTE, KLINE_INTERVAL_30MINUTE),
        (KLINE_INTERVAL_1HOUR, KLINE_INTERVAL_1HOUR),
        (KLINE_INTERVAL_2HOUR, KLINE_INTERVAL_2HOUR),
        (KLINE_INTERVAL_4HOUR, KLINE_INTERVAL_4HOUR),
        (KLINE_INTERVAL_6HOUR, KLINE_INTERVAL_6HOUR),
        (KLINE_INTERVAL_8HOUR, KLINE_INTERVAL_8HOUR),
        (KLINE_INTERVAL_12HOUR, KLINE_INTERVAL_12HOUR),
        (KLINE_INTERVAL_1DAY, KLINE_INTERVAL_1DAY),
        (KLINE_INTERVAL_3DAY, KLINE_INTERVAL_3DAY),
        (KLINE_INTERVAL_1WEEK, KLINE_INTERVAL_1WEEK),
        (KLINE_INTERVAL_1MONTH, KLINE_INTERVAL_1MONTH),
    )
    
    buy_sell = models.CharField(max_length=10, choices=BUY_SELL_CHOICES)
    order_type = models.CharField(max_length=200, choices=ORDER_TYPE_CHOICES, default=LIMIT)
    volume = models.DecimalField(decimal_places=18, max_digits=36, default=10000)
    price = models.DecimalField(decimal_places=18, max_digits=36, default=0.005)# Default value change
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default=NEW)
    contract_type = models.CharField(max_length=200, choices=CONTRACT_TYPE_CHOICES, default=SPOT)
    trading_pair = models.ForeignKey(TradingPair, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class ordermachmodel(models.Model):
    
    pair = models.ForeignKey(TradingPair, on_delete=models.CASCADE)
    timeframe = models.CharField(max_length=200, choices=Order.TIMEFRAME_CHOICES)
      

    #def __str__(self):
    #    return f"{self.contract_number}"


class getexchangepricemodel(models.Model):# Analize all market 
    
    pair = models.ForeignKey(TradingPair, on_delete=models.CASCADE)
    timeframe = models.CharField(max_length=200, choices=Order.TIMEFRAME_CHOICES)
    exchange = models.CharField(max_length=200)
    number_of_candel = models.CharField(max_length=200)

    #def __str__(self):
    #    return f"{self.contract_number}"