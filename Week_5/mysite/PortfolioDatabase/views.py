from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Hobby
from .models import Project


# Create your views here.
def Home(request):
    return HttpResponse('Welcome to my Portfolio. My name is Richard Heiner. I have an Associates Degree in General'
                        'Studies and in Computer Science. I am working on my Bachelors Degree in Computer Science.'
                        'So far I have enjoyed programming in multiple languages, including: Python, Java, Javascript,'
                        'and C++.')


def Hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'portfolio/index.html', context)


def Portfolio(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list,
    }
    return render(request, 'portfolio/index.html', context)


def Contact(request):
    return HttpResponse('Here is my email address: feinerheiner91@gmail.com')


def hobby_detail(request, item_id):
    item = Hobby.objects.get(pk=item_id)
    name = item.hobby_name
    desc = item.hobby_desc
    context = {
        'item': item,
        'name': name,
        'desc': desc,
    }
    return render(request, 'portfolio/detail.html', context)


def project_detail(request, item_id):
    item = Project.objects.get(pk=item_id)
    name = item.project_name
    desc = item.project_desc
    context = {
        'item': item,
        'name': name,
        'desc': desc,
    }
    return render(request, 'portfolio/detail.html', context)


