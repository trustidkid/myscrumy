from django import forms
from django.contrib.auth.models import User
from .models import ScrumyGoals
from django.forms import ModelForm

# Lab 19 starts here
"""
    SignupForm and CreateGoalForm. The signup form will contain fields from the User model such as first_name,last_name,email,username,password and the CreateGoalForm will contain the goal_name field and user field from the ScrumyGoals model. The user field will enable a user of your application select the particular user the goal is being created for
    """


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'username', 'password']


class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']


class MoveGoal(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_status']
