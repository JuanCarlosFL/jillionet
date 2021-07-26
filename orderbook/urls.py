from django.urls import path

from .views import OrderCreateView, OrderListView


app_name = 'orderbook'


urlpatterns = [
    path('', OrderListView.as_view(), name='orderbook'),
    path('<slug:slug>/', OrderCreateView.as_view(), name='create_order'),
]