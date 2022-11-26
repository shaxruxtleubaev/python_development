from django.urls import path
from .views import home_page_users

urlpatterns = [
    path('', home_page_users)
]