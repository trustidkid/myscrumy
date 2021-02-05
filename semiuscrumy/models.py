from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GoalStatus(models.Model):
    scrumy_name = models.CharField()


    def __str__(self):
        return self.scrumy_name

class ScrumyGoals(models.Model):
    #goal_name, goal_id, created_by, moved_by, owner
    goal_id = models.BigIntegerField()
    goal_name = models.CharField()
    created_by = models.CharField()
    moved_by = models.CharField()
    owner = models.CharField()
    goal_status = models.ForeignKey(GoalStatus,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='scrumygoals')
    
    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    #moved_by, created_by, moved_from, moved_to, time_of_action
    created_by = models.CharField()
    moved_by = models.CharField()
    moved_from = models.CharField()
    moved_to = models.CharField()
    time_of_action = models.CharField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.created_by

