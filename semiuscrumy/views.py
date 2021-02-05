from django.shortcuts import render
from django.http import HttpResponse
from semiuscrumy.models import ScrumyGoals, ScrumyHistory, GoalStatus

# Create your views here.
def get_grading_parameters(request): 
    return HttpResponse("This is a Scrum Application")
