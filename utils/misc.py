import datetime
import json
from decimal import Decimal
from orderbook.models import Order
from statistics import mean, StatisticsError


def entries_to_remove(entries, the_dict):
    for key in entries:
        the_dict.pop(key, None)
    return the_dict


def get_number_of_months(start_month, start_yr, end_month, end_yr):
    end_date = datetime.datetime(end_yr, end_month, 1)
    start_date = datetime.datetime(start_yr, start_month, 1)
    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    return num_months


# this get the minimum non zero item
def get_min_non_zero(arr):
    new_arr = [i for i in arr if i > 0]
    if len(new_arr) == 0:
        return 1
    m = min(new_arr)
    return m


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def get_thousandth(num):
    return round(Decimal(num)/1000) * 1000


def get_jill_bid():
    buy_order_qs = Order.objects.filter(buy_sell=Order.BUY, trading_pair__pair='JILL/EUR', status=Order.FILL).order_by('price')
    
    #get_exchange_price()

    bid_list = buy_order_qs[:10]
    
    try:
        bid_price = mean([x.price for x in bid_list])
    except StatisticsError:
        bid_price = 0
    
    return bid_price


def get_jill_ask():
    sell_order_qs = Order.objects.filter(buy_sell=Order.SELL, trading_pair__pair='JILL/EUR', status=Order.FILL).order_by('-price')
    ask_list = sell_order_qs[:10]
    
    try:
        ask_price = mean([x.price for x in ask_list])
    except StatisticsError:
        ask_price = 0

    return ask_price
