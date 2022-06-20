from django.db import models
from django.contrib.auth.models import User as Editor
from location_field.models.plain import PlainLocationField

# Create your models here.


class NeighbourHood(models.Model):
	picture = models.ImageField(upload_to = 'hoodimages/', blank=True, null=True)
	name = models.CharField(max_length=30)
	location = PlainLocationField(based_fields=['city'], zoom=7)
	Occupants_count = models.IntegerField(default=0)
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE, blank=True, null= True)

	@classmethod
	def get_all(cls):
		business =  cls.objects.all()
		return business

	@classmethod
	def get_by_id(cls, id):
			table = NeighbourHood.objects.get(id=id)
			return table

class User(models.Model):
	picture = models.ImageField(upload_to = 'userimages/', blank=True, null=True)
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=255)
	NeighbourHood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE, blank=True, null= True)
	
	def __str__(self):
			return str(self.id)

	@classmethod
	def get_by_user(cls, editor):
		profile = User.objects.filter(editor__username=editor).last()
		return profile

class Business(models.Model):
	picture = models.ImageField(upload_to = 'businessimages/', blank=True, null=True)
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

class Posts(models.Model):
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE, blank=True, null= True)
	neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, blank=True, null= True)
	post = models.TextField(max_length=255)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.post

	@classmethod
	def get_by_project(cls, id):
		table = NeighbourHood.objects.get(project_id=id)
		return table

class Contacts(models.Model):
	neighbourHood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
	police = models.IntegerField()
	hospital = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return str(self.id)

	@classmethod
	def get_by_neighbourhood(cls, id):
		table = Contacts.objects.get(neighbourHood_id=id)
		return table