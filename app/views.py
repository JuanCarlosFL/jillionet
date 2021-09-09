
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

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
    template_name = 'iabotcontract.html'


class SettingsView(TemplateView):
    template_name = 'coming_soon.html'


class DappsView(TemplateView):
    template_name = 'coming_soon.html'


class HoldersView(TemplateView):
    template_name = 'coming_soon.html'


class MultiwayView(TemplateView):
    template_name = 'coming_soon.html'


class BroadcastView(TemplateView):
    template_name = 'coming_soon.html'


class NftsView(TemplateView):
    template_name = 'coming_soon.html'


class Contract(TemplateView):
    template_name = 'contract.html'
