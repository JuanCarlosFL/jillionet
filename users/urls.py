from django.urls import path

from .views import UserBalanceView

app_name = 'users'


urlpatterns = [
    path('balance/', UserBalanceView.as_view(), name='balance')
]
