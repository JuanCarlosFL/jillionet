from django.urls import path

from .views import MarketListView
from yeildfarming.views import YeildContractListView
from .views import iabotListView
from IaBotpredict.views import iabottable

app_name = 'app'


urlpatterns = [
    path('market/', MarketListView.as_view(), name='market'),
    path('yeild/', YeildContractListView.as_view(), name='yeild'),
    path('iabot/', iabotListView.as_view(), name='iabot'),
    path('ia/', iabottable.as_view(), name='ia'),

]
