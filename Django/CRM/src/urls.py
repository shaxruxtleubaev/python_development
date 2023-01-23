from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from quotes.views import Register

urlpatterns = [
    path('register/success/',
         TemplateView.as_view(template_name='registration/success.html'),
         name='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('admin/', admin.site.urls),
    path('quote/', include('quotes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
    path('', include('pages.urls')),
]

