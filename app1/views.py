from django.shortcuts import render
from django.http import HttpResponse

def string1(request):
    return HttpResponse('<h1> This is my first project in app1</h1>')


def string2(request):
    return HttpResponse('<h1> This my sencond project in app2 </h1> ')
    
