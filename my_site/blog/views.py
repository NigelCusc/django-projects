import json
from django.core.paginator import Paginator
from django.http import Http404
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

# ALL POSTS W PAGINATION
def index(request):
    # sort the posts by date in descending order
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    # map the posts to the mapper function
    mapped_posts = [mapper(post) for post in sorted_posts]
    paginator = Paginator(mapped_posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})

# SINGLE POST
def post_detail(request, slug):
    post = next((post for post in posts if post['slug'] == slug), None)
    if not post:
        raise Http404("Post not found")
    return render(request, 'blog/post_detail.html', {'post': mapper(post)})