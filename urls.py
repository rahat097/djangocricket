from django.urls import path
#from . import views
from . views import cricketgame



urlpatterns = [
    #path('', views.home, name='home'),
    #path('allpost/', AllPostView, name='allpost'),
    path('cricket/<int:pk>', cricketgame, name='cricketgame'),




    ]