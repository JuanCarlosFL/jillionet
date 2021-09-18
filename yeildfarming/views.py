from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.contrib import messages


from .models import YeildContract, YeildOrderBook
from users.models import UserLevel


class YeildContractListView(ListView):
    model = YeildContract
    template_name = 'contract.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'user_levels': UserLevel.objects.all()
        })

        return context


class BuyContractView(LoginRequiredMixin, CreateView):
    model = YeildOrderBook
    fields = ['contract_pair']
    success_url = reverse_lazy('app:yeild')

    def get_success_url(self):
        messages.success(self.request, f'You successfully bought the <strong>{self.object.contract_pair.yeildpair}</strong> contract')
        return super().get_success_url()
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
