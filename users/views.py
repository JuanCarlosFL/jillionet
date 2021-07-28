from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserBalance
from orderbook.models import Order

class UserBalanceView(ListView):
    model = UserBalance
    template_name = 'users/balance.html'
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update({
            'order_history': Order.objects.filter(user=self.request.user, status=Order.FILL),
            'open_orders': Order.objects.filter(user=self.request.user, status=Order.NEW)
        })

        return context


class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'users/order_history.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user, status=Order.FILL)