from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    peoples = [
        {'name': 'Abhijeet Singh', 'age':26 },
        {'name': 'lodha Singh', 'age':17 },
        {'name': 'Tau Singh', 'age':53 }
    ]
    context = {'page': 'index'}
    return render(request,"home/index.html",context ={'page': 'Django 2023 tutorial', 'peoples': peoples})

def about(request):
    context = {'page': 'about'}
    return render(request , "home/about.html",context)

def contact(request):
    context={'page':'contact'}
    return render(request , "home/contact.html",context)






