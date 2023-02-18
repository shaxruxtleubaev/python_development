from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Shop

def mainPage(request):
    return render(request, 'base.html', {})

class ShopListView(ListView):

    model = Shop
    template_name = 'market/shop_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shops'] = Shop.objects.all()
        return context

class ShopDetailView(DetailView):

    context_object_name = 'Shops'
    queryset = Shop.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shops'] = Shop.objects.all()
        return context

