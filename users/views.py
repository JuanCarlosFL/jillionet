import json
from decimal import Decimal

from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserBalance, BalanceFor
from orderbook.models import Order


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


class UserBalanceView(LoginRequiredMixin, ListView):
    model = UserBalance
    template_name = 'users/balance.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        balances = BalanceFor.objects.all()

        # total_fund = [{x.name: list(self.request.user.get_balance(x))} for x in balances]
        total_fund = {}
        for x in balances:
            total_fund[x.name] = list(self.request.user.get_balance(x))
        # print(json.dumps(total_fund, cls=DecimalEncoder))

        context.update({
            'order_history': Order.objects.filter(user=self.request.user, status=Order.FILL),
            'open_orders': Order.objects.filter(user=self.request.user, status=Order.NEW),
            'balances': balances,
            'all_fund_json': json.dumps(total_fund, cls=DecimalEncoder)
        })

        return context


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'users/order_history.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user, status=Order.FILL)