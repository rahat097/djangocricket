from django.urls import path
#from . import views
from . views import cricketgame,crickethome,cricketaccept,cricketdelete



urlpatterns = [
    path('', crickethome, name='crickethome'),
    #path('allpost/', AllPostView, name='allpost'),
    path('<int:pk>', cricketgame, name='cricketgame'),
    path('accept/<int:id>', cricketaccept, name='cricketaccept'),
    path('delete/<int:id>', cricketdelete, name='cricketdelete'),




    ]