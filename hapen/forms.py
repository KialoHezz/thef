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