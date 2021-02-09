from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus
from django.contrib.auth.models import User

# Create your views here.


def get_grading_parameters(request):
    #goal = ScrumyGoals.objects.filter(goal_name = "Learn Django")
    #return HttpResponse("Learn Django")
    dic_values = {
        "goal_name": "Learn Django", #ScrumyGoals.objects.get(goal_name = "Learn Django"),
        "goal_id": 1, #ScrumyGoals.objects.get(goal_id=1),
        "user": "Louis" #User.objects.get(username="Louis")
    }
    return render(request, 'semiuscrumy/home.html', {"goal_name" : "Learn Django" })

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goal_id=1)
    goalname = goal.goal_name
    return HttpResponse(goalname)





