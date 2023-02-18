from django.contrib import admin
from .models import Shop, Category

class ShopAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'user')
    list_display_links = ('id',)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    list_display_links = ('id',)

admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)