from django.shortcuts import render
from django.contrib.auth.models import User
from . models import Cricket
from .forms import Cricketrun


def cricketgame(request,pk):
	game = Cricket.objects.get(pk=pk)
	if game.user1out == False:
		if request.method == 'POST':
			form = Cricketrun(request.POST)

			if form.is_valid():
				hit = request.POST['hit']
				hit = int(hit)
				if request.user == game.user1:
					game.user1lastbat = hit
					if game.user1lastbat != game.user2lastball:
						game.user1run = game.user1run + game.user1lastbat
						game.user1hit = game.user1hit + 1
					else:
						game.user1out = True
						game.user1hit = 0
						game.user2hit = 0
					game.save()
				if request.user == game.user2:
					game.user2lastball = hit
					game.user2hit = game.user2hit + 1
					game.save()
			

		else:
			form = Cricketrun()
	else:
		if request.method == 'POST':
			form = Cricketrun(request.POST)

			if form.is_valid():
				hit = request.POST['hit']
				hit = int(hit)
				if request.user == game.user2:
					game.user2lastbat = hit
					if game.user2lastbat != game.user1lastball:
						game.user2run = game.user2run + game.user2lastbat
						game.user2hit = game.user2hit + 1
						if game.user2run > game.user1run:
							game.gameend = True
							game.gameresult = f'{game.user2} Won The game'
					else:
						game.user2out = True
						game.gameend = True
						if game.user1run == game.user2run:
							game.gameresult = 'This game is Draw'
						else:
							game.gameresult = f'{game.user2} Won the Game'

					game.save()
				if request.user == game.user1:
					game.user1lastball = hit
					game.user1hit = game.user1hit + 1
					game.save()
			

		else:
			form = Cricketrun()

	targetrun = game.user1run + 1
	context = {
	'game' : game,
	'form' : form,
	'targetrun' : targetrun
	}


	return render(request, 'cricket.html',context)
