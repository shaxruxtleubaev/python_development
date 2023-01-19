from django.shortcuts import render
from django.http import HttpResponseRedirect
from quotes.models import Quote
from .forms import QuoteForm
from pages.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured

class QuoteList(ListView):
	model = Quote
	template_name = 'quotes/quote_list.html'
	context_object_name = 'all_quotes' #default -> object_name

class QuoteDetail(DetailView):
	model = Quote
	context_object_name = 'quote' #default -> object 

	def get_context_data(self, **kwargs):
		context = super(QuoteDetail, self).get_context_data(**kwargs)
		context['page_list'] = Page.objects.all()
		return context

#START REGISTRATION LABEL

class Register(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register-success')

	def get_success_url(self):
		if not self.success_url:
			raise ImproperlyConfigured("NO url to redirect")
		return str(self.success_url)

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(self.success_url)

#END REGISTRATION LABEL

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