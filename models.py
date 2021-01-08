from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Cricket(models.Model):
	user1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user1')
	user1run = models.PositiveIntegerField(default=0)
	user1hit = models.PositiveIntegerField(default=0)
	user1lastbat = models.PositiveIntegerField(default=0)
	user1out = models.BooleanField(default=False)
	user1lastball = models.PositiveIntegerField(default=0)
	user2 = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='user2')
	user2run = models.PositiveIntegerField(default=0)
	user2hit = models.PositiveIntegerField(default=0)
	user2lastbat = models.PositiveIntegerField(default=0)
	user2out = models.BooleanField(default=False)
	user2lastball = models.PositiveIntegerField(default=0)
	gameend = models.BooleanField(default=False)
	gameresult = models.TextField(blank=True,null = True)



	def __str__(self):
		return str(self.id)+'  ' + str(self.user1.username) +'  '+ str(self.user2.username)