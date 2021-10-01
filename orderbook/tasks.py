import json
from decimal import Decimal

from celery import Celery
from binance.client import Client
from django.conf import settings

from .models import JillPrice, Order
from utils.misc import DecimalEncoder, get_thousandth

client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)

app = Celery()


@app.task
def get_jillion_price_data():
    # client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)
    btcusdt_ticker = client.get_ticker(symbol='BTCUSDT')
    last_jillion_price = Order.objects.filter(
        buy_sell=Order.SELL, trading_pair__pair='JILL/EUR', status=Order.FILL
    ).order_by('-timestamp').first().price

    jill_price_ticker = {
        "symbol": "JILLEUR",

        "lastPrice": Decimal(btcusdt_ticker["lastPrice"])/get_thousandth(btcusdt_ticker["lastPrice"])*last_jillion_price,

        "lowPrice": btcusdt_ticker["lowPrice"],

        "openTime": btcusdt_ticker["openTime"],
        "closeTime": btcusdt_ticker["closeTime"],

    }
    btcusdt_ticker_json = json.dumps(jill_price_ticker, cls=DecimalEncoder)
    # print(btcusdt_ticker_json)
    JillPrice.objects.create(data=btcusdt_ticker_json)
