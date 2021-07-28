from django.contrib import admin

from .models import iabotcontract, iabotOrderbook

@admin.register(iabotcontract)
class iabotadmin(admin.ModelAdmin):
    list_display = ['pair']


@admin.register(iabotOrderbook)
class iabotOrderbook(admin.ModelAdmin):
    list_display = ['pair']