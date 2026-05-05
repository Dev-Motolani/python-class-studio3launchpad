from django.urls import path
from .models import Post
from .forms import BlogCreateForm


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'