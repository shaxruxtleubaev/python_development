from django.urls import path
#from api.views import students, Home, home_page, student
from api.views.studets import students, student

urlpatterns = [
    path('', students),
    path('<int:pk>/', student)
]

"""
path('', students),
path('<int:pk>/', student),
#path('', Home.as_view()),
path('teachers/', home_page)
"""