from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus

# Create your views here.

def get_grading_parameters(request):
    goal = ScrumyGoals.objects.filter(goal_name = "Learn Django")
    return HttpResponse(goal)


#def move_goal(request, goal_id):
    #goal = ScrumyGoals.objects.get(goal_name="Learn Django")
    #goalname = response.goal_name
    #return HttpResponse(goal)
