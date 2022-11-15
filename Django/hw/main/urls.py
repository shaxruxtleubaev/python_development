from django.contrib import admin
from django.urls import path
from one.views import one_front
from two.views import two_front

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', one_front),
    path('', two_front)
]

