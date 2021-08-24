from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserBalance, BalanceFor
from orderbook.models import Order


class UserBalanceView(LoginRequiredMixin, ListView):
    model = UserBalance
    template_name = 'users/balance.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        balances = BalanceFor.objects.all()

        context.update({
            'order_history': Order.objects.filter(user=self.request.user, status=Order.FILL),
            'open_orders': Order.objects.filter(user=self.request.user, status=Order.NEW),
            'balances': balances
        })

        return context


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'users/order_history.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user, status=Order.FILL)