
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.conf import settings
from django.utils import timezone

from tradingview_ta import TA_Handler, Interval
from binance.client import Client
from binance.enums import *

from orderbook.models import TradingPair
from yeildfarming.models import YeildContract
from IaBotpredict.models import iabotcontract

def index(request):

    return render(request, 'inicio.html', {})


class MarketListView(ListView):
    model = TradingPair
    template_name = 'app/market.html'


    ##((BTC/x+ETH/X)/2)*(Lastorderbook price)
    ##

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        symbol_list = [symbol.get_symbol.lower() for symbol in self.object_list if 'jill' not in symbol.get_symbol.lower()]
        jill_symbol_list = [symbol.get_symbol.lower() for symbol in self.object_list if 'jill' in symbol.get_symbol.lower()]

        context.update({
            'symbol_list': symbol_list,
            'jill_symbol_list': jill_symbol_list
        })

        return context

class yeildwatchListView(ListView):
    model = YeildContract
    template_name = 'yeildcontrac.html'


class iabotListView(ListView):
    model = iabotcontract
    template_name = 'app/jillbot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        client = Client(settings.BINANCE_API_KEY, settings.BINANCE_API_SECRET, tld='com')

        now = timezone.now()
        fecha = now.strftime("%d-%m-%y %H:%M:%S")

        lista = ([{'symbol': 'BTCUSDT'},{'symbol': 'ETHUSDT'},{'symbol': 'LTCUSDT'},{'symbol': 'EOSUSDT'},{'symbol': 'IOTAUSDT'},{'symbol': 'TRXUSDT'},{'symbol': 'ATOMUSDT'},{'symbol': 'LINKUSDT'},{'symbol': 'ENJUSDT'},{'symbol': 'IOSTUSDT'}])

        ####################################
        
        result = []

        for i in lista:
            tesla = TA_Handler()
            tesla.set_symbol_as(i['symbol'])
            tesla.set_exchange_as_crypto_or_stock("BINANCE")
            tesla.set_screener_as_crypto()
            tesla.set_interval_as(Interval.INTERVAL_15_MINUTES)
            vela = client.get_klines(symbol=(i['symbol']), interval=Client.KLINE_INTERVAL_15MINUTE)
            
            #print(i['symbol'])
            #print("ultimo precio")
            #print(vela[0][4])

            try:        
                #print(tesla.get_analysis().interval)
                #print(tesla.get_analysis().summary)
                #input("Presione una tecla para continuar...")
                analysis = {
                    'symbol': i['symbol'],
                    'price': vela[0][4],
                    'interval': tesla.get_analysis().interval,
                    'summary': tesla.get_analysis().summary
                }

                result.append(analysis)
            except Exception as e:
                print("No Data")
            continue

        print(result)

        context.update({
            'analysis': result
        })

        return context


class SettingsView(TemplateView):
    template_name = 'coming_soon.html'


class DappsView(TemplateView):
    template_name = 'coming_soon.html'


class HoldersView(TemplateView):
    template_name = 'app/holders.html'


class MultiwayView(TemplateView):
    template_name = 'coming_soon.html'


class BroadcastView(TemplateView):
    template_name = 'app/broadcast.html'


class NftsView(TemplateView):
    template_name = 'app/nfts.html'


class Contract(TemplateView):
    template_name = 'contract.html'
