from django.shortcuts import render
from django.views.generic.list import ListView

from .models import iabotcontract


class iabottable(ListView):
    model = iabotcontract
    templete_name = 'iabotcontract.html'