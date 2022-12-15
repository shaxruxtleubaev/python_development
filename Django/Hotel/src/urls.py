from django.contrib import admin
from django.urls import path
from room.views import post_list, post_retrieve, post_create, post_update, post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/', post_list),
    path('listings/<int:pk>/', post_retrieve),
    path('listings/create/', post_create),
    path('listings/<int:pk>/edit/', post_update),
    path('listings/<int:pk>/delete/', post_delete)
]
