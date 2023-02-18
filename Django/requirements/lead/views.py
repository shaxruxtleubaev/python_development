from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Bb
from .models import Rubric
from .forms import BbForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def index(request):
    template = loader.get_template('lead/by_index.html')
    rubrics = Rubric.objects.all()
    bbs = Bb.objects.all()
    context = {
        'bbs' : bbs,
        'rubrics': rubrics,
    }
    return HttpResponse(template.render(context, request))

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs' : bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'lead/by_rubric.html', context)

class BbCreateView(CreateView):
    template_name = 'lead/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context