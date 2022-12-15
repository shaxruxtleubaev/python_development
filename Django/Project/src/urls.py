from django.contrib import admin
from django.urls import path
from app.views import app_list, app_product, app_update, app_delete, app_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', app_list),
    path('app/create/', app_create),
    path('app/<int:pk>/', app_product),
    path('app/<int:pk>/update/', app_update),
    path('app/<int:pk>/delete/', app_delete)
]
