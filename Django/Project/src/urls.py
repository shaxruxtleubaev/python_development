from django.contrib import admin
from django.urls import path
from app.views import app_list, app_product, app_update, app_delete, app_create
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', app_list),
    path('app/create/', app_create),
    path('app/<int:pk>/', app_product),
    path('app/<int:pk>/update/', app_update),
    path('app/<int:pk>/delete/', app_delete)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

