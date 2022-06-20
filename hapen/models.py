from django.db import models
from django.contrib.auth.models import User as Editor
from location_field.models.plain import PlainLocationField

# Create your models here.


class NeighbourHood(models.Model):

	name = models.CharField(max_length=30)
	location = PlainLocationField(based_fields=['city'], zoom=7)
	Occupants_count = models.IntegerField(default=0)

	@classmethod
	def get_all(cls):
		business =  cls.objects.all()
		return business


class User(models.Model):
   
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=255)
	NeighbourHood_id = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE, blank=True, null= True)


	@classmethod
	def get_by_user(cls, editor):
		profile = cls.objects.filter(editor__username=editor).last()
		return profile

class Business(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)   
	user_name = models.ForeignKey(User, on_delete=models.CASCADE)  
	neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, blank=True, null= True)

	@classmethod
	def search_by_title(cls,search_term):
		busines = cls.objects.filter(title__icontains=search_term)
		return busines

	@classmethod
	def get_all(cls):
		business =  cls.objects.all()
		return business