from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import BlogCreateForm
from django.urls import reverse_lazy

class PostListView(ListView):
    #List all posts
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    #Show details of a post
    model = Post
    template_name = 'blogs/detail.html'


class PostCreateView(CreateView):
    #Create a new post
    model = Post
    form_class = BlogCreateForm
    template_name = 'blogs/create.html'
    success_url = reverse_lazy('home')