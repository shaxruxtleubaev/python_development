from django.urls import path
from .views import one_front

urlpatterns = [
    path('', one_front),
]
