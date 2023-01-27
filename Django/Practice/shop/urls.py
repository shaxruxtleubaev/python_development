from django.urls import path
from shop.views import ProductListView, ProductDetailView, Order

urlpatterns = [
    path('<slug:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='product_list'),
]