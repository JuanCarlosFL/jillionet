from django.urls import path

from .views import BuyContractView

app_name = 'yeildfarming'


urlpatterns = [
    path('buy/', BuyContractView.as_view(), name='buy-contract'),
]