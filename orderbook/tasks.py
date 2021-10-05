import json
from decimal import Decimal

from celery import Celery
from binance.client import Client
from django.conf import settings

from .models import JillPrice, Order
from utils.misc import DecimalEncoder, get_thousandth, get_jill_bid, get_jill_ask

client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)

app = Celery()


def get_price(buy_sell):

    btcusdt_ticker = client.get_ticker(symbol='BTCUSDT')
    if buy_sell == JillPrice.SELL:
        last_jillion_price = get_jill_bid()
    else:
        last_jillion_price = get_jill_ask()

    jill_price_ticker = {
        "symbol": "JILLEUR",

        "lastPrice": Decimal(btcusdt_ticker["lastPrice"])/get_thousandth(btcusdt_ticker["lastPrice"])*last_jillion_price,

        "lowPrice": btcusdt_ticker["lowPrice"],

        "openTime": btcusdt_ticker["openTime"],
        "closeTime": btcusdt_ticker["closeTime"],

    }
    btcusdt_ticker_json = json.dumps(jill_price_ticker, cls=DecimalEncoder)
    # print(btcusdt_ticker_json)
    JillPrice.objects.create(data=btcusdt_ticker_json, buy_sell=buy_sell)


@app.task
def get_jillion_price_data():
    # client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)
    get_price(JillPrice.SELL)
    get_price(JillPrice.BUY)
