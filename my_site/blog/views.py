from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')

def post_detail(request, slug):
    return render(request, 'blog/post_detail.html', {
        'title': 'Post Detail',
        'slug': slug,
    })