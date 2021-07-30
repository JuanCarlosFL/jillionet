
import os
from binance.client import Client

api_key = "3IyANOhqv4ka3vQWswY3Nkxf4Jii1z5u4Ee3z9odX1YI2fBfZXAay6INcWOuHMYf"
api_secret = "ARqGpw44UOGSfJPCcZRvuWxzJPk0N9Tk1Jo2AGf6mDylpZHGK7YqCYbDGH1rzCzI"

client = Client(api_key, api_secret  , tld='com')

velaBTC = client.get_klines(symbol='BTCEUR', interval=Client.KLINE_INTERVAL_1MINUTE)


CloseBTC =(velaBTC[0][4])

print (CloseBTC)            
    