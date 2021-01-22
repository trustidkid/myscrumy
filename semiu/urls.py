from django.urls import path
from semiu import views
urlpatterns = [
    path('', views.index)
]
