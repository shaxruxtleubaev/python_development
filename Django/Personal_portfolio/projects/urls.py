from django.urls import path
from .views import project_index, project_detail

urlpatterns = [
    path('<int:pk>/', project_detail, name='project_detail'),
    path('', project_index, name='project_index')
]
