from django.contrib import admin

from .models import YeildContract, YeildOrderBook

@admin.register(YeildContract)
class yeildfarmAdmin(admin.ModelAdmin):
    list_display = ['yeildpair', 'liquidity','APR','APYd365','d30','d7','d1' ]


@admin.register(YeildOrderBook)
class YeildOrderBookAdmin(admin.ModelAdmin):
    list_display = ['contract_pair', 'status','user','volume','coin_reward','volume','Jill_reward' ]