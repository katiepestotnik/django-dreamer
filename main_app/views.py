from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('DREAM ENGINEER')

def about(request):
    return HttpResponse('About page')