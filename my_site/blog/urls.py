from django.urls import path
from .views import index, post_detail

app_name = 'blog-posts'

urlpatterns = [
    path('', index, name='index'), # List of all posts
    path('<str:slug>/', post_detail, name='post_detail'), # Detail view for a specific post
]