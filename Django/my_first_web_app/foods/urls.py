from django.urls import path
from .views import foods_list, foods_detail

urlpatterns = [
    path('<int:pk>/', foods_detail, name='food_detail'),
    path('', foods_list, name='food_list'),
]
