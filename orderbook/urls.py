from django.urls import path

from .views import OrderCreateView, OrderListView, AllOrderView


app_name = 'orderbook'


urlpatterns = [
    path('', AllOrderView.as_view(), name='all_orderbook'),
    path('<slug:slug>/', OrderListView.as_view(), name='orderbook'),
    path('<slug:slug>/', OrderCreateView.as_view(), name='create_order'),
]