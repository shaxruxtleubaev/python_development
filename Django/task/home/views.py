from django.shortcuts import render
from .models import Home

def home(request):
    
    home = Home.objects.all()
    context = {
         'home': home
    }
    return render(request, 'home/home_page.html', context)

def home_details(request, pk):
    
    homes = Home.objects.get(id=pk)
    context = {
         'homes': homes
    }
    return render(request, 'home/home_page_details.html', context)

