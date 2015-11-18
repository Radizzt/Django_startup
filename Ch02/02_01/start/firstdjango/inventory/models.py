from django.db import models

#creating a class that inherits from modes.Model
class Item(models.Model):
	title = models.CharField(max_length=200);
	description = models.TextField();
	amount = models.IntegerField();