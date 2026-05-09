from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,
 PostUpdateView, PostDeleteView, AboutView)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', AboutView.as_view(), name='about'),
]