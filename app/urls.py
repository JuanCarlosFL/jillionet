from django.urls import path

from .views import (MarketListView, SettingsView,
                    DappsView, MultiwayView, HoldersView,
                    BroadcastView, NftsView, Contract
                    )
from yeildfarming.views import YeildContractListView
from .views import iabotListView
from IaBotpredict.views import iabottable

app_name = 'app'


urlpatterns = [
    path('market/', MarketListView.as_view(), name='market'),
    path('yeild/', YeildContractListView.as_view(), name='yeild'),
    path('iabot/', iabotListView.as_view(), name='iabot'),
    path('ia/', iabottable.as_view(), name='ia'),

    path('settings/', SettingsView.as_view(), name='settings_view'),
    path('dapps/', DappsView.as_view(), name='dapps'),
    path('holders/', HoldersView.as_view(), name='holders'),
    path('multiway/', MultiwayView.as_view(), name='multiway'),
    path('broadcast/', BroadcastView.as_view(), name='broadcast'),
    path('nfts/', NftsView.as_view(), name='nfts'),
    path('contract/', Contract.as_view(), name='contract'),

]
