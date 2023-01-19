from django.urls import path
from quotes.views import quote_req
from quotes.views import QuoteList
from quotes.views import QuoteDetail

urlpatterns = [
	path('', quote_req, name='quote-req'),
	path('show/<int:pk>/', QuoteDetail.as_view(), name='quote-detail'),
	path('show', QuoteList.as_view(), name='show-quotes'),
]	


##fsdsdv