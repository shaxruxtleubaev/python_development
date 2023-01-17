from django.shortcuts import render
from django.http import HttpResponseRedirect
from quotes.models import Quote
from .forms import QuoteForm
from pages.models import Page

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
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted
	}
	return render(request, 'quotes/quote.html', context)    

