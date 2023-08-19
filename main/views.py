from django.shortcuts import render
from .models import Project


def main(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'main/home.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'main/project.html', context)