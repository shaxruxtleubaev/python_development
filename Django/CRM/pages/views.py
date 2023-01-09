from django.shortcuts import render
from .models import *

def home(request):
    #pagename = '/' + pagename
    #pg = Page.objects.get(permalink=pagename)
    context = {
        #'title': pg.title,
        #'content': pg.body_text,
        #'last_updated': pg.update_date,
        'page_list': Page.objects.all()
    }
    return render(request, 'pages/page_list.html', context)
