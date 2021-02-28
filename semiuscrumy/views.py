from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import ScrumyGoals, GoalStatus
from django.contrib.auth.models import User, Group
from .forms import SignupForm, CreateGoalForm, MoveGoal
import random


# Create your views here.


def index(request):
    # lab 8 soluution
    # return HttpResponse("This is a Scrum Application")
    # goal = ScrumyGoals.objects.filter(goal_name="Learn Django")

    # solution for Lab 20
    """ Your task is to Edit your index view such that a user is added to the group “Developer” on account creation. Ensure that the user is directed to a page that says “Your account has been created successfully” if the operation was successful """

    # get the group name
    developer_group = Group.objects.get(name='Developer')

    # Lab 20 starts here

    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # solution lab 19
            username = form.cleaned_data['username']
            form.save()
            
            userid = User.objects.get(username=username)
            userid.groups.add(developer_group)
            #group.user_set.add(username)
            
            return HttpResponse('Your account has been created successfully')
    else:
        form = SignupForm()
    return render(request, 'semiuscrumy/index.html', {'form': form})


def move_goal(request, goal_id):

    form = MoveGoal()
    if request.method == 'POST':
        form = MoveGoal(request.POST)
        if form.is_valid():
            # get current login user
            user = request.user
            goal_status = form.cleaned_data['goal_status']
            
            # check if the belong to the specified group
            # The user can move his goal to all goal status except done status
            if user.groups.filter(name='Developer').exists():
                #check that he is the owner of the goal
                if user == ScrumyGoals.objects.get(goal_id=goal_id).owner: #and form.cleaned_data['goal_name'] == 'Weekly Goal':
                    if goal_status == 'Done Goal':
                        return HttpResponse('You do not have permission to move goal to this status ')
                    else:
                        ScrumyGoals.objects.filter(goal_id=goal_id).update(goal_status_id = goal_status)
                        return HttpResponse('Goal move was successfully')
            # User can move goal to all status except Weekly Goal
            elif user.groups.filter(name='Quality Assurance').exists():
                #check theat user is the owner of the goal and the goal is a 'weekly goal'
                if user == ScrumyGoals.objects.get(goal_id=goal_id).owner: #and form.cleaned_data['goal_name'] == 'Weekly Goal':
                    if goal_status == 'Weekly Goal':
                        return HttpResponse('You do not have permission to move this goal')
                    else:
                        
                        ScrumyGoals.objects.filter(goal_id=goal_id).update(goal_status_id = goal_status)
                        return HttpResponse('Goal was moved successfully')
                else:
                    #QA can only move another user goal from 'verify goal' to 'done goal'
                    if ScrumyGoals.objects.get(goal_id=goal_id).goal_name == 'Verify Goal': #and form.cleaned_data['goal_name'] == 'Done Goal':
                        ScrumyGoals.objects.filter(goal_id=goal_id).update(goal_status_id = goal_status)
                        return HttpResponse('Goal was moved successfully')
             #Owner can move goal to anywhere       
            elif user.groups.filter(name='Owner').exists():
                ScrumyGoals.objects.filter(goal_id=goal_id).update(goal_status_id = goal_status)
                return HttpResponse('Goal was moved successfully')

            # admin can move goal to any of the status
            else:
                ScrumyGoals.objects.filter(goal_id=goal_id).update(goal_status_id = goal_status)
                return HttpResponse('Goal was moved successfully')
        else:
            form = MoveGoal()
    goal_name = ScrumyGoals.objects.get(goal_id=goal_id)
    return render(request, 'semiuscrumy/movegoal.html', {'form': form, 'goal_name': goal_name})

    # lab 15 starts here -- works locally but fail the test
    # dictionary = {
    # }
    # try:
    #    goalname = obj.goal_name
    #    return HttpResponse(goalname)
   # except Exception as e:
    # ScrumyGoals.DoesNotExist:
    #   return render(request, 'semiuscrumy/exception.html', dictionary)
    # lab 15 ends here


def add_goal(request):
    # lab18 solutions for quesion no. 3

    #get current login user
    user = request.user
    
    form = CreateGoalForm()

    if request.method == 'POST':
        form = CreateGoalForm(request.POST)
        if form.is_valid:
            if user.groups.filter(name='Developer').exists():
                if user == form.cleaned_data['user'] and form.cleaned_data['goal_name'] == 'Weekly Goal':
                    goalid = random.randint(1000, 9999)
                    updatefield = form.save(commit=False)
                    updatefield.goal_id = goalid
                    updatefield.goal_name = form.cleaned_data['goal_name']
                    updatefield.created_by = form.cleaned_data['user']
                    updatefield.moved_by = form.cleaned_data['user']
                    updatefield.owner = form.cleaned_data['user']
                    statusid = GoalStatus.objects.get(
                        status_name='Weekly Goal')
                    updatefield.goal_status_id = statusid.id
                    userid = User.objects.get(username=form.cleaned_data['user'])
                    updatefield.user_id = userid.id
                    updatefield.save()
                    return HttpResponse('New Goal Added Successfully')
                
            elif user.groups.filter(name='Quality Assurance').exists():
                if user == form.cleaned_data['user'] and form.cleaned_data['goal_name'] == 'Weekly Goal':
                    goalid = random.randint(1000, 9999)
                    updatefield = form.save(commit=False)
                    updatefield.goal_id = goalid
                    updatefield.goal_name = form.cleaned_data['goal_name']
                    updatefield.created_by = form.cleaned_data['user']
                    updatefield.moved_by = form.cleaned_data['user']
                    updatefield.owner = form.cleaned_data['user']
                    statusid = GoalStatus.objects.get(
                        status_name='Weekly Goal')
                    updatefield.goal_status_id = statusid.id
                    userid = User.objects.get(username=form.cleaned_data['user'])
                    updatefield.user_id = userid.id
                    updatefield.save()
                    return HttpResponse('New Goal Added Successfully')
            #Owner column
            elif user.groups.filter(name='Owner').exists():
                if user == form.cleaned_data['user'] and form.cleaned_data['goal_name'] == 'Weekly Goal':
                    goalid = random.randint(1000, 9999)
                    updatefield = form.save(commit=False)
                    updatefield.goal_id = goalid
                    updatefield.goal_name = form.cleaned_data['goal_name']
                    updatefield.created_by = form.cleaned_data['user']
                    updatefield.moved_by = form.cleaned_data['user']
                    updatefield.owner = form.cleaned_data['user']
                    statusid = GoalStatus.objects.get(
                        status_name='Weekly Goal')
                    updatefield.goal_status_id = statusid.id
                    userid = User.objects.get(username=form.cleaned_data['user'])
                    updatefield.user_id = userid.id
                    updatefield.save()
                    return HttpResponse('New Goal Added Successfully')
            else:
                return HttpResponse('You can not create goal for another user')
    else:
        form = CreateGoalForm()
        return render(request, 'semiuscrumy/addgoal.html', {'form':
                                                            form})

    # Task: goal_name = ‘Keep Learning Django’ goal_id = a randomly generated integer between 1000 and 9999 created_by = ‘Louis’ moved_by = ‘Louis’ owner = ‘Louis’ goal_status = a Weekly goal instance of the GoalStatus model user = an instance of the User model(Louis Oma)

    # Solutions starts here
    # goalstatus = GoalStatus.objects.get(status_name='Weekly Goal')
    # user = User.objects.get(username='louis')
    # generate random goal_id
    # goalid = random.randint(1000, 9999)
    # savegoal = ScrumyGoals(goal_id=goalid, goal_name='Keep Learning Django', created_by='Louis',
     #                      moved_by='Louis', owner='Louis', goal_status=goalstatus, user=user)
    # savegoal.save()
    # return HttpResponse(savegoal)


def home(request):
    # response = GoalStatus.objects.filter(goal_name="Keep Learning Django")
    # Lab 16 starts here
    # I) all existing users on the User model.
    # II) every goal that falls under Weekly Goals
    # II) All goals under Daily Goals
    # IV) All goals under Verify Goals
    # V) All goals under Done Goals

    """
    weekly_goals = ScrumyGoals.objects.filter(
        goal_status=GoalStatus.objects.get(status_name='Weekly Goal'))
    daily_goals = ScrumyGoals.objects.filter(
        goal_status=GoalStatus.objects.get(status_name='Daily Goal'))
    verify_goals = ScrumyGoals.objects.filter(
        goal_status=GoalStatus.objects.get(status_name='Verify Goal'))
    done_goals = ScrumyGoals.objects.filter(
        goal_status=GoalStatus.objects.get(status_name='Done Goal'))
    """
    # count users
    user = User.objects.all()
    # all scrumy goals
    # check login user
    loginuser = request.user
    scrumygoals = ScrumyGoals.objects.all()
    context = {'users': user, 'scrumygoals':
               scrumygoals, 'loginuser': loginuser}
    return render(request, 'semiuscrumy/home.html', context)
    

# lab 16 stops here

    # lab 14 solutions - works
 #   context = {
    # ScrumyGoals.objects.get(goal_name="Learn Django"),
   #     'goal_name': ScrumyGoals.objects.get(goal_name="Learn Django"),
   #     'goal_id': 1,
   #     'user': User.objects.get(username="louis")
   # }
  #  return render(request, 'semiuscrumy/home.html', context)
    # lab 14 ends here


# return HttpResponse(response)
