from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus
from django.contrib.auth.models import User

# Create your views here.


def get_grading_parameters(request):
    #goal = ScrumyGoals.objects.filter(goal_name = "Learn Django")
    # return HttpResponse("Learn Django")
    dictionary = {
        # ScrumyGoals.objects.get(goal_name = "Learn Django"),
        'goal_name': 'Learn Django',
        'goal_id': ScrumyGoals.objects.get(goal_id=1),
        'user': User.objects.get(username="Louis")
    }
    return render(request, 'semiuscrumy/home.html', dictionary)


def move_goal(request, goal_id):
    obj = ScrumyGoals.objects.get(goal_id=goal_id)
    if obj:
        #goal = ScrumyGoals.objects.get(goal_id=goal_id)
        goalname = obj.goal_name
        return HttpResponse(goalname)
    else:
        return render(request, 'semiuscrumy/exception.html', {'error': 'A record with that goal id does not exist'})
