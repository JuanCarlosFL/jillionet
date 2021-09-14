from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy

from .models import YeildContract, YeildOrderBook


class YeildContractListView(ListView):
    model = YeildContract
    template_name = 'contract.html'


class BuyContractView(LoginRequiredMixin, CreateView):
    model = YeildOrderBook
    fields = ['contract_pair']
    success_url = reverse_lazy('app:yeild')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
