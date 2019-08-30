from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	sid = models.CharField(max_length=5,unique=True)
	sname = models.CharField(max_length=50)
	singer = models.CharField(max_length=50)
	cost = models.IntegerField()
	file = models.FileField(upload_to='musics/songs',blank=True)
	desc = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.sname

class Try(models.Model):
	gender = models.CharField(max_length=40)
	date   = models.DateField(auto_now_add=False)
	image  = models.ImageField(blank=False)

	def __str__(self):
		return self.gender


