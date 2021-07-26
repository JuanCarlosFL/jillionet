from django.shortcuts import render
from django.views.generic.list import ListView

from .models import UserBalance

class UserBalanceView(ListView):
    model = UserBalance
    template_name = 'users/balance.html'
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)