from django.urls import path

from .views import MarketListView

app_name = 'app'


urlpatterns = [
    path('market/', MarketListView.as_view(), name='market'),
]
