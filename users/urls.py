from django.urls import path

from .views import UserBalanceView, OrderHistoryView

app_name = 'users'


urlpatterns = [
    path('balance/', UserBalanceView.as_view(), name='balance'),
    path('order-history/', OrderHistoryView.as_view(), name='order_history')
]
