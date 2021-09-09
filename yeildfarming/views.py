from django.shortcuts import render
from django.views.generic.list import ListView

from .models import YeildContract


class YeildContractListView(ListView):
    model = YeildContract
    template_name = 'contract.html'