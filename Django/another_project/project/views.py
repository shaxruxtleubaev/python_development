from django.shortcuts import render
from project.models import Blog, Authors


def project_index(request):
    projects = Blog.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'project/project_index.html', context)


def project_detail(request, pk):
    project = Blog.objects.get(id=pk)
    context = {
        "project": project
    }
    return render(request, 'project/project_detail.html', context)
