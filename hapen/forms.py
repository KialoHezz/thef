from .models import Posts,Comment
from django.forms import ModelForm
from django import forms


class PostForm(forms.Form):
    class Meta:
        model = Posts
        fields = ('name', 'post')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['name',  'content']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "content": forms.Textarea(attrs={'class': 'form-control'})

        }

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

