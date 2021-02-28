from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'semiuscrumy'
urlpatterns = [
    path('', views.index, name='index'),
    path('/movegoal/<int:goal_id>', views.move_goal, name='movegoal'),
    path('/addgoal', views.add_goal, name='addgoal'),  # lab 18
    path('/home', views.home, name='home'),  # lab 17 added url name
    # Lab 17 starts here
    path('/accounts/', include('django.contrib.auth.urls'))

]
