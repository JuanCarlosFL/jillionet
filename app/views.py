
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

class yeildwatchListView(ListView):
    model = yeildcontract
    template_name = 'yeildcontrac.html'

class iabotListView(ListView):
    model = iabotcontract
    template_name = 'iabotcontract.html'
