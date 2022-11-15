from django.shortcuts import render
from django.http import HttpResponse

def two_front(request):
    return HttpResponse('<h2>This is second message</h2>')
