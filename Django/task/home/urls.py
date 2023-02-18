from django.urls import path
from .views import home, home_details

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', home_details, name='home_details'),
]