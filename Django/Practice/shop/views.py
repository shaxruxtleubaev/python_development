from django.shortcuts import render
from shop.models import Product, Customer, Order, OrderItem, ShippingAddress
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from shop.forms import ContactForm
from django.core.mail import send_mail, get_connection
from django.http import HttpResponseRedirect

class ProductListView(ListView):
    template_name = 'shop/home_page.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.all()