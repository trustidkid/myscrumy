from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.get_grading_parameters),
    path('/movegoal/<int:goal_id>', views.move_goal),
    path('/addgoal', views.add_goal),
    path('/home', views.home, name='index'),  # lab 17 added url name
    # Lab 17 starts here
    path('/accounts/', include('django.contrib.auth.urls'))

]
