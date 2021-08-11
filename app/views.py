
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from orderbook.models import TradingPair
from yeildfarming.models import yeildcontract
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
    model = yeildcontract
    template_name = 'yeildcontrac.html'


class iabotListView(ListView):
    model = iabotcontract
    template_name = 'iabotcontract.html'
