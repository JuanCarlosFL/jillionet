from django.contrib import admin
from .models import Historicaldata


@admin.register(Historicaldata)
class HistoricaldataAdmin(admin.ModelAdmin):
    list_display = ['symbol',]