from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quote/', include('quotes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
]

