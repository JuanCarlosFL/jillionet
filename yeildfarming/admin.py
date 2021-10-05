from django.contrib import admin

from .models import YeildContract, YeildOrderBook

@admin.register(YeildContract)
class yeildfarmAdmin(admin.ModelAdmin):
    list_display = ['yeildpair', 'liquidity','APR','APYd365','d30','d7','d1' ]


@admin.register(YeildOrderBook)
class YeildOrderBookAdmin(admin.ModelAdmin):
    list_display = ['contract_pair', 'status','user','format_volume', 'timestamp']

    def format_volume(self, obj):
        return round(obj.volume, 2)
    format_volume.short_description = 'Volume'
    format_volume.admin_order_field = 'volume'