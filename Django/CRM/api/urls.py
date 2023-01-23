from django.urls import path
from .views import routes

urlpatterns = [
    path('', routes)
]