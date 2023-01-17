from django.shortcuts import render
from django.http import HttpResponseRedirect

from quotes.models import Quote
from .forms import QuoteForm
from pages.models import Page

from django.views.generic.list import ListView

class QuoteList(ListView):
	model = Quote
	template_name = 'quotes/quote_list.html'
	context_object_name = 'all_quotes' #default -> object_name


def quote_req(request):
	submitted = False 
	if request.method == 'POST':
		form = QuoteForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/quote?submitted=True')
	else:
		form = QuoteForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form' : form,
		'page_list' : Page.objects.all(),
		'submitted' : submitted
	}
	return render(request, 'quotes/quote.html', context)
