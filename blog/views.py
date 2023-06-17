from django.shortcuts import render, get_object_or_404
from .models import Post


def get_date(post):
    p = post['date']
    return p

# Create your views here.

def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request , "blog/index.html", {"posts": latest_post})


def post(request):
    return render(request, "blog/all_post.html", {"posts":Post.objects.all().order_by("-date")})

def post_slug(request, slug):
    identify_post = get_object_or_404(Post, slug = slug)
    return render(request, "blog/post-detail.html", {"post": identify_post})

