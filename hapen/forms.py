from django import forms
from .models import Business, Contacts, NeighbourHood, User


class BusinessForm(forms.ModelForm):
		class Meta:
			model = Business		
			exclude = ['user_name','neighbourhood'] 


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