from django.urls import path
from pages.views import home
from pages.views import contact

urlpatterns = [
	path('', home, {'pagename': ''}, name='home'),
	path('contact', contact, name='contact'),
	path('<str:pagename>', home, name='index')
]
