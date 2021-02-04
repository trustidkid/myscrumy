from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GoalStatus(models.Model):
    scrumy_name = models.CharField(max_length=200)

    #class Meta:
       # app_label = 'semiuscrumy'

    def __str__(self):
        return self.scrumy_name

class ScrumyGoals(models.Model):
    goal_id = models.IntegerField(default=1)
    goal_name = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    moved_by = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    goal_status = models.ForeignKey(GoalStatus,on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='scrumygoals')
    
    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    created_by = models.CharField(max_length=200)
    moved_by = models.CharField(max_length=200)
    moved_from = models.CharField(max_length=200)
    moved_to = models.CharField(max_length=200)
    time_of_action = models.CharField(max_length=200)
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.created_by

