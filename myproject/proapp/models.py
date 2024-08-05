from django.db import models
class User(models.Model):
	username=models.CharField(max_length=64)
	password=models.IntegerField()
	email=models.CharField(max_length=64)
	first_name=models.CharField(max_length=64)
	last_name=models.CharField(max_length=64)