from django.urls import path
from .models import Post



class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'author']