from django.db import models

#Create your models here.


class Accounts(models.Model):
	username  = models.CharField(max_length=40)
	email     = models.EmailField()
	password  = models.CharField(max_length=8)
	conf_password = models.CharField(max_length=8)

