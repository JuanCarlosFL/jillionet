from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Order, TradingPair


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    success_url = '/'
    success_message = 'Order successfully created'
    fields = ['buy_sell', 'trading_pair', 'order_type', 'volume']    

    def get_initial(self):
        trading_pair = TradingPair.objects.filter(slug=self.kwargs.get('slug'))
        return {
            'trading_pair': trading_pair.first().id
        }

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class OrderListView(ListView):
    model = Order
    template_name = 'orderbook/orderbook.html'