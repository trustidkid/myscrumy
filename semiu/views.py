from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
def get_grading_parameters(request): 
    return HttpResponse("Welcome to Django")
def index(request):
    return HttpResponse("You are welcome to Django")