from django.contrib import admin

from .models import Order, Currency, TradingPair, getexchangepricemodel


@admin.register(TradingPair)
class TradingPairAdmin(admin.ModelAdmin):
    list_display = ['pair', 'slug']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'buy_sell', 'status', 'trading_pair','volume','price']
    search_fields = ['buy_sell', 'user__username', 'trading_pair__pair']

    #def get_chain(self, obj):
    #    return obj.currency.chain
    #get_chain.short_description = 'Currency Chain'
    #get_chain.admin_order_field = 'currency__chain'


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'chain', 'name','default_public_key','contract_creator_hash']


@admin.register(getexchangepricemodel)
class getexchangepricemodelAdmin(admin.ModelAdmin):
    list_display = ['pair', 'exchange']