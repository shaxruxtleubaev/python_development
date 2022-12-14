from django.contrib import admin
from django.urls import path
from room.views import post_list, post_retrieve, post_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', post_list),
    path('listings/<int:pk>/', post_retrieve),
    path('listings/create/', post_create)
]
