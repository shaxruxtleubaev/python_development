from django.shortcuts import render
from django.http import HttpResponse

def one_front(request):
    return HttpResponse('<h1>This is first message</h1>')
