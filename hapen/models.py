from django.db import models
from django.contrib.auth.models import User as Editor
# from location_field.models.plain import PlainLocationField
from django.utils import timezone

# Create your models here.


class NeighbourHood(models.Model):
	picture = models.ImageField(upload_to = 'hoodimages/')
	name = models.CharField(max_length=30)
	location =  models.CharField(max_length=30)
	Occupants_count = models.IntegerField(default=0)
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE)

	
	def __str__(self):
			return self.name


	@classmethod
	def get_all(cls):
		business =  cls.objects.all()
		return business

	@classmethod
	def get_by_id(cls, id):
			table = NeighbourHood.objects.get(id=id)
			return table

	@classmethod
	def get_by_name(cls, name):
			table = NeighbourHood.objects.get(name=name)
			return table

class User(models.Model):
	picture = models.ImageField(upload_to = 'userimages/')
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=255)
	Neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE)

	
	def __str__(self):
			return str(self.id)

	@classmethod
	def get_by_user(cls, editor):
		profile = User.objects.filter(editor__username=editor).last()
		return profile

class Business(models.Model):

	picture = models.ImageField(upload_to='businessimages/', blank=True, null=True)
	name = models.CharField(max_length=255)
	business_type = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)   
	number = models.IntegerField()
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
	neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)

	@classmethod
	def search_by_name(cls,search_term):
		business = Business.objects.filter(name__icontains=search_term)
		return business

	@classmethod
	def get_all(cls):
		business =  cls.objects.all()
		return business

class Posts(models.Model):
	editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
	neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
	post = models.TextField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
	profile = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.post

	@classmethod
	def get_by_project(cls, id):

		table = NeighbourHood.objects.get(project_id=id)
		return table


class Contacts(models.Model):
	neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
	police = models.IntegerField()
	hospital = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return str(self.id)

	@classmethod
	def get_by_neighbourhood(cls, id):

		table = Contacts.objects.filter(neighbourhood_id=id).last()
		return table

