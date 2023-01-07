from django.urls import path
from .views import *

urlpatterns = [
    path('', mainPage, name='home'),
    path('shops/<slug:slug>/', ShopDetailView.as_view(), name='shop_detail'),
    path('shops/', ShopListView.as_view(), name='shop_list')
]