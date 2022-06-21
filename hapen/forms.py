from django import forms
from .models import Business, Contacts, NeighbourHood, User, Posts


class BusinessForm(forms.ModelForm):
		class Meta:
			model = Business		
			exclude = ['editor','neighbourhood'] 


class ContactsForm(forms.ModelForm):
		class Meta:
			model = Contacts		
			exclude = ['neighbourhood', 'date'] 

class NeighbourHoodForm(forms.ModelForm):
		class Meta:
			model = NeighbourHood		
			exclude = ['editor'] 	

class UserForm(forms.ModelForm):
		class Meta:
			model = User		
			exclude = ['editor'] 	

class PostsForm(forms.ModelForm):
		class Meta:
			model = Posts		
			exclude = ['editor', 'neighbourhood','profile'] 	