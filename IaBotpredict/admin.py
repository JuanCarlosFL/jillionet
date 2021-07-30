from django.contrib import admin

from .models import iabotcontract, iabotOrderbook

@admin.register(iabotcontract)
class iabotadmin(admin.ModelAdmin):
    list_display = ['contract_number', 'pair', 'timeframe', 'win_close_point', 'lose_close_point']


@admin.register(iabotOrderbook)
class iabotOrderbook(admin.ModelAdmin):
    list_display = ['pair']