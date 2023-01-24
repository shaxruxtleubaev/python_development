from django.contrib import admin
from shop.models import Product

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'digital',)
    list_display_links = ('name',)

admin.site.register(Product, ProductAdmin)