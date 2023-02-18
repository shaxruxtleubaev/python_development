from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'project/project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        "project": project
    }
    return render(request, 'projects/project_detail.html', context)
