from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus
from django.contrib.auth.models import User
import random

# Create your views here.


def get_grading_parameters(request):
    # lab 8 soluution
    # return HttpResponse("This is a Scrum Application")
    goal = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(goal)


def move_goal(request, goal_id):
    # lab 15 statrts here -- works locally but fail the test
    dictionary = {
        'error': 'A record with that goal id does not exist'
    }
    try:
        obj = ScrumyGoals.objects.get(goal_id=goal_id)
    except Exception as e:
        # ScrumyGoals.DoesNotExist:
        return render(request, 'semiuscrumy/exception.html', dictionary)
    else:
        # goalname = obj.goal_name
        return HttpResponse(obj.goal_name)
    # lab 15 ends here


def add_goal(request):
    # goal_name = ‘Keep Learning Django’ goal_id = a randomly generated integer between 1000 and 9999 created_by = ‘Louis’ moved_by = ‘Louis’ owner = ‘Louis’ goal_status = a Weekly goal instance of the GoalStatus model user = an instance of the User model(Louis Oma)
    goalstatus = GoalStatus.objects.get(scrumy_name='Weekly Goal')
    user = User.objects.get(username='louis')
    # generate random goal_id
    goalid = random.randint(1000, 9999)
    savegoal = ScrumyGoals(goal_id=goalid, goal_name='Keep Learning Django', created_by='Louis',
                           moved_by='Louis', owner='Louis', goal_status=goalstatus, user=user)
    savegoal.save()
    return HttpResponse(savegoal)


def home(request):
    # response = GoalStatus.objects.filter(goal_name="Keep Learning Django")

    # lab 14 solutions - works
    """
    context = {
        # ScrumyGoals.objects.get(goal_name="Learn Django"),
        'goal_name': ScrumyGoals.objects.get(goal_name="Learn Django"),
        'goal_id': 1,
        'user': User.objects.get(username="louis")
    }
    return render(request, 'semiuscrumy/home.html', context)
    # lab 14 ends here
    """
    # Lab 16 starts here
    # I) all existing users on the User model.
    # II) every goal that falls under Weekly Goals
    # II) All goals under Daily Goals
    # IV) All goals under Verify Goals
    # V) All goals under Done Goals

    weekly = GoalStatus.objects.get(scrumy_name='Weekly Goal')
    daily = GoalStatus.objects.get(scrumy_name='Daily Goal')
    verify = GoalStatus.objects.get(scrumy_name='Verify Goal')
    done = GoalStatus.objects.get(scrumy_name='Done Goal')
    # count users
    usercount = User.objects.all().count()
    # build array of goal id
    goal_id_array = []

    if usercount > 0:
        for gd in range(1, usercount):
            count = ScrumyGoals.objects.all()
            ids = count[gd].goal_id
            goal_id_array.append(ids)

        context = {
            'goalid': ScrumyGoals.objects.all()[0].goal_id,
            # all existing users in the model
            'users': User.objects.all()[0].username,
            'weeklygoal': weekly.goalstatus.all()[0].goal_name,
            'dailygoal': daily.goalstatus.all()[0].goal_name,
            'verifygoal': verify.goalstatus.all(),
            'done': done.goalstatus.all()
        }
        return render(request, 'semiuscrumy/home.html', context)
    # return HttpResponse(response)
