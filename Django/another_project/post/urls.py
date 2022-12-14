from django.urls import path
from .views import post_list, post_detail, post_form

urlpatterns = [
    path('post/', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('new/', post_form, name='post_form'),
]
