from django.shortcuts import render
from django.views.generic.list import ListView

from .models import yeildcontract


class YeildContractListView(ListView):
    model = yeildcontract
    template_name = 'yeildcontrac.html'