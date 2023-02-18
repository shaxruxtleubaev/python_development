from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Food

def foods_list(request):
    
    foods = Food.objects.all()
    context = {
         'foods': foods
    }
    return render(request, 'foods/food_list.html', context)

def foods_detail(request, pk):
    food = Food.objects.get(id=pk)
    context = {
        'food': food
    }
    return render(request, 'foods/food_detail.html', context)


