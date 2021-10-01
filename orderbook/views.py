import json
from statistics import mean, StatisticsError

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Order, TradingPair, JillPrice
from .controller import get_mathing_order
from historicalData.controller import get_exchange_price


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
        get_mathing_order(self.object)
        return reverse("orderbook:orderbook", args=[self.kwargs.get('slug')])

    def get_initial(self):
        trading_pair = TradingPair.objects.filter(slug=self.kwargs.get('slug')).first()
        buy_order_qs = self.model.objects.filter(buy_sell=Order.BUY, trading_pair=trading_pair, status=Order.NEW).order_by('-price')
        sell_order_qs = self.model.objects.filter(buy_sell=Order.SELL, trading_pair=trading_pair, status=Order.NEW).order_by('-price')
        initial_vals = {
            'trading_pair': trading_pair.id,
            'buy_orders': buy_order_qs,
            'sell_orders': sell_order_qs
        }

        if buy_order_qs.exists():
            price = round(buy_order_qs.last().price, 2)
            initial_vals.update({
                'price': price
            })

        return initial_vals

    def form_valid(self, form):
        # TODO: get market price and replace if market is selected in order form

        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trading_pair = TradingPair.objects.filter(slug=self.kwargs.get('slug')).first()

        #get_exchange_price()

        bid_list = self.get_initial().get('buy_orders')[:10]
        try:
            bid_price = mean([x.price for x in bid_list])
        except StatisticsError:
            bid_price = 0
        print(bid_price, len(bid_list))

        jill_chart_data = [json.loads(jill_price.data) for jill_price in JillPrice.objects.all()]

        context.update({
            'buy_orders': self.get_initial().get('buy_orders'),
            'sell_orders': self.get_initial().get('sell_orders'),
            'trading_pair': trading_pair,
            'all_order': self.model.objects.all(),
            'open_orders': self.model.objects.filter(status=Order.NEW),
            'current_price': self.get_initial().get('price'),
            'bid_price': bid_price,
            'jill_chart_data': jill_chart_data
        })
        return context


def get_half_jillion_price(request, slug):

    #(ask+bid)/2
    trading_pair = TradingPair.objects.get(slug=slug)

    #buy_order_qs = Order.objects.filter(buy_sell=Order.BUY, trading_pair=trading_pair, status=Order.NEW).order_by('-price')
    sell_order_qs = Order.objects.filter(buy_sell=Order.SELL, trading_pair=trading_pair, status=Order.FILL).order_by('-timestamp')
       

    return JsonResponse(data={
        'last_price': sell_order_qs.first().price
    })


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