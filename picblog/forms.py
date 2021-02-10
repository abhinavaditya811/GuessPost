from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields= ('title', 'author', 'body', 'header_image', 'answer')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control','value':'','id':'naam'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'answer': forms.TextInput(attrs={'class':'form-control'})
        }   

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields= ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }