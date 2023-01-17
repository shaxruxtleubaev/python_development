from django.urls import path
from quotes.views import quote_req
from quotes.views import QuoteList

urlpatterns = [
	path('show', QuoteList.as_view(), name='show-quotes'),
	path('', quote_req, name='quote-req'),
]
