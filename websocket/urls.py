from django.urls import path, include
from .views import views

urlpatterns = [
     path('test/', views.test, name='test'),
     path('connect/', views.connect, name = 'connect'),
     path('disconnect/', views.disconnect, name = 'disconnect'),
     path('send_message/', views.send_message, name = 'sendmessage'),
     path('getrecentmessage/', views.getRecentMessages, name = 'recentmessage')
     
     
]