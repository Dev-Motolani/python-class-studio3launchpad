from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('home', PostListView.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
]