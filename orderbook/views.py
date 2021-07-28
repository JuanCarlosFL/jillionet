from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Order, TradingPair


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    success_url = '/'
    success_message = 'Order successfully created'
    fields = ['buy_sell', 'trading_pair', 'order_type', 'volume','price']    

    def get_initial(self):
        trading_pair = TradingPair.objects.filter(slug=self.kwargs.get('slug'))
        return {
            'trading_pair': trading_pair.first().id
        }

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class OrderListView(CreateView):
    model = Order
    template_name = 'orderbook/orderbook.html'
    success_message = 'Order successfully created'
    fields = ['buy_sell', 'trading_pair', 'order_type', 'volume','price']

    def get_success_url(self):
        return reverse("orderbook:orderbook", args=[self.kwargs.get('slug')])

    def get_initial(self):
        trading_pair = TradingPair.objects.filter(slug=self.kwargs.get('slug')).first()
        buy_order_qs = self.model.objects.filter(buy_sell=Order.BUY, trading_pair=trading_pair).order_by('-price')
        sell_order_qs = self.model.objects.filter(buy_sell=Order.SELL, trading_pair=trading_pair).order_by('price')
        
        return {
            'trading_pair': trading_pair.id,
            'price': round(buy_order_qs.last().price, 2),
            'buy_orders': buy_order_qs,
            'sell_orders': sell_order_qs
        }

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trading_pair = TradingPair.objects.filter(slug=self.kwargs.get('slug')).first()        

        context.update({
            'buy_orders': self.get_initial().get('buy_orders'),
            'sell_orders': self.get_initial().get('sell_orders'),
            'trading_pair': trading_pair
        })
        return context

class AllOrderView(ListView):
    model = Order
    template_name = 'orderbook/orderbook.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        buy_order_qs = self.model.objects.filter(buy_sell=Order.BUY)
        sell_order_qs = self.model.objects.filter(buy_sell=Order.SELL)

        context.update({
            'buy_orders': buy_order_qs,
            'sell_orders': sell_order_qs
        })
        return context