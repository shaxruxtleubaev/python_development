from django.urls import path
from .views import two_front

urlpatterns = [
    path('', two_front),
]

