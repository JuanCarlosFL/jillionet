
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from orderbook.models import TradingPair


def index(request):

    return render(request, 'inicio.html', {})


class MarketListView(ListView):
    model = TradingPair
    template_name = 'app/market.html'

