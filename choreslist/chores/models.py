from django.db import models

#creat your models here

class CharList(models.Model):
	name = models.CharField(max_length = 100)
	due_date = models.DateTimeField()

class Chore(models.Model):
	chore_list = models.ForeignKey(CharList)
	name = models.CharField(max_length = 100)
	due_date = models.DateTimeField()

	