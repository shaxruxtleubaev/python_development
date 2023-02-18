from django.shortcuts import render
from django.http import HttpResponse
from .models import Three

def three_front(request):
     
    three = Three.objects.all()
    context = {
        'three': three
    }
    return render(request, 'index3.html', context)