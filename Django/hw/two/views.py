from django.shortcuts import render
from django.http import HttpResponse
from .models import Two

def two_front(request):
    two = Two.objects.all()
    context = {
        'two': two
    }
    return render(request, 'index1.html', context)