import json
from django.shortcuts import render

posts = json.load(open('data/posts.json'))

def mapper(post):
    return {
        'slug': post['slug'],
        'title': post['title'],
        'image': post['image'],
        'date': post['date'],
        'excerpt': post['excerpt'],
        'content': post['content'],
    }

def index(request):
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    mapped_posts = [mapper(post) for post in sorted_posts]
    # limit to latest 3 posts
    latest_posts = mapped_posts[:3]
    return render(request, 'home/index.html', {'latest_posts': latest_posts})