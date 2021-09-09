from django.contrib import admin

from .models import YeildContract

@admin.register(YeildContract)
class yeildfarmAdmin(admin.ModelAdmin):
    list_display = ['yeildpair', 'liquidity','APR','APYd365','d30','d7','d1' ]