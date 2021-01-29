from django.urls import path
from semiuscrumy import views
urlpatterns = [
    path('', views.get_grading_parameters)
]