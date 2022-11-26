from django.urls import path
from .views import three_front

urlpatterns = [
    path('', three_front)
]