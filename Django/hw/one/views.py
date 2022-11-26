from django.shortcuts import render
from django.http import HttpResponse
from .models import One

def one_front(request):
    
    one = One.objects.all()
    context = {
        'one': one
    }
    return render(request, 'index.html', context)
