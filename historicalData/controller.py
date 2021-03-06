
import os
from binance.client import Client
from celery import Celery

app = Celery()

from orderbook.models import getexchangepricemodel, Order, TradingPair
from historicalData.models import Historicaldata

api_key = "3IyANOhqv4ka3vQWswY3Nkxf4Jii1z5u4Ee3z9odX1YI2fBfZXAay6INcWOuHMYf"
api_secret = "ARqGpw44UOGSfJPCcZRvuWxzJPk0N9Tk1Jo2AGf6mDylpZHGK7YqCYbDGH1rzCzI"
client = Client(api_key, api_secret  , tld='com')



#connect with API Binance CCXT API to get all the coins price

@app.task
def get_exchange_price():
    print('HERE')
    exchange_pairs = getexchangepricemodel.objects.all()

    for pair in exchange_pairs:
                           
        candel = client.get_klines(symbol=pair.pair.get_symbol, interval=Client.KLINE_INTERVAL_1MINUTE, limit=1000)
        Historicaldata.objects.create(symbol=pair.pair.get_symbol, data=candel)
        #print(candel[0])
        Close =(candel[0][4])
        Open =(candel[0][1])
        High =(candel[0][3])
        Low =(candel[0][2])
        #print (CloseBTC)
        
    #getexchangepricemodel.objects.create(pair=trading_pair, timeframe=Order.KLINE_INTERVAL_1MINUTE, number_of_candels=4, exchange=CloseBTC)   




#!/usr/bin/env python

#import os
#from binance.client import Client
#import config
#import pandas as pd



#client = Client(config.API_KEY, config.API_SECRET , tld='com')


# intervalos válidos - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M


# obtenemos el timestamp de la fecha más reciente que está disponible
#timestamp = client._get_earliest_valid_timestamp('BTCUSDT', '15m')


# hacemos una petición de los datos históricos (or klines) 
#bars = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE,limit=10 )



#orderbook = client.get_order_book(symbol='BTCUSDT')


#orderbook = pd.DataFrame(bars, columns=['1', '2', '3','4','5', '6', '7','8','9', '10', '11','12'])
#orderbook.set_index('1', inplace=True)
#print(orderbook.head())

# exportamos el líbro de ordenes en un archivo csv 

#orderbook.to_csv('orderbook.csv')

#historico = pd.DataFrame(bars, columns=['Opentime', 'Open', 'High', 'Low', 'Close','Volume', 'Closetime', 'AsetVolume', 'Trades', 'TBBAV', 'TBQAV', 'ignore'])
#historico.set_index('Opentime', inplace=True)
#print(historico.head())

# exportamos el histórico

#historico.to_csv('historico.csv')