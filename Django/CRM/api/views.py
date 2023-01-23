from django.http import JsonResponse
from .links import products

def routes(request):
    links = [
        'api/quote/show/'
        'accounts/login/'
    ]
    return JsonResponse(links, safe=False)

