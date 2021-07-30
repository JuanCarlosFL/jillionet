from django.urls import path

from .views import MarketListView
from .views import yeildwatchListView
from .views import iabotListView
from IaBotpredict.views import iabottable

app_name = 'app'


urlpatterns = [
    path('market/', MarketListView.as_view(), name='market'),
    path('yeild/', yeildwatchListView.as_view(), name='yeild'),
    path('iabot/', iabotListView.as_view(), name='iabot'),
    path('ia/', iabottable.as_view(), name='ia'),

]
