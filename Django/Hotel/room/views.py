from django.shortcuts import render
from .models import Listings

#CRUD -> Create Retrieve Update Delete

def post_list(request):
    listings = Listings.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'post_list.html', context)
    #return render(request, 'post_list.html', {'listings': listings})

def post_retrieve(request, pk):
    listing = Listings.objects.get(id=pk)
    context = {
        'listing':listing
    }
    return render(request, 'post_retrieve.html', context)

def post_create(request):
    return render(request, 'post_create.html')


