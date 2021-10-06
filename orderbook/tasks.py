import json
from decimal import Decimal

from celery import Celery
from binance.client import Client
from django.conf import settings

from .models import JillPrice, Order
from utils.misc import DecimalEncoder, get_thousandth, get_jill_bid, get_jill_ask

client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET)

app = Celery()


@app.task
def get_jillion_price_data():
    btcusdt_ticker = client.get_ticker(symbol='BTCUSDT')

    jill_price_ticker = {
        "symbol": "JILLEUR",

        "lastBidPrice": Decimal(btcusdt_ticker["lastPrice"]) / get_thousandth(
            btcusdt_ticker["lastPrice"]) * get_jill_bid(),
        "lastAskPrice": Decimal(btcusdt_ticker["lastPrice"]) / get_thousandth(
            btcusdt_ticker["lastPrice"]) * get_jill_ask(),

        "lowPrice": btcusdt_ticker["lowPrice"],

        "openTime": btcusdt_ticker["openTime"],
        "closeTime": btcusdt_ticker["closeTime"],

    }
    btcusdt_ticker_json = json.dumps(jill_price_ticker, cls=DecimalEncoder)
    # print(btcusdt_ticker_json)
    JillPrice.objects.create(data=btcusdt_ticker_json)
