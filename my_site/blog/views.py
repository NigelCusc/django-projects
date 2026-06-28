from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Post

# ALL POSTS W PAGINATION
def index(request):
    # sort the posts by date in descending order
    sorted_posts = Post.objects.all().order_by("-date")
    paginator = Paginator(sorted_posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})

# SINGLE POST
def post_detail(request, slug):
    # Find or raise 404 error if post not found
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})