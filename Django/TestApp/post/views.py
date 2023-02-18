from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article

class ArticleListView(ListView):
    template_name = 'post/post_index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'post/post_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.all()
