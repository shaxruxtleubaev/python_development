from django.contrib import admin
from django.urls import path
from one.views import one_front
from two.views import two_front
from three.views import three_front
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/one_front/', include('one.urls')),
    path('project/two_front/', include('two.urls')),
    path('project/three_front/', include('three.urls')),
]

