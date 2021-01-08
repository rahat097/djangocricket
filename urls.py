from django.urls import path
#from . import views
from . views import cricketgame,crickethome



urlpatterns = [
    path('', crickethome, name='crickethome'),
    #path('allpost/', AllPostView, name='allpost'),
    path('<int:pk>', cricketgame, name='cricketgame'),




    ]