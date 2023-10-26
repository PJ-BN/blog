from django.shortcuts import render, get_object_or_404 , redirect
from .models import *


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

def add(request):
    
    
    return render(request, "blog/add.html")

def adddata(request):
    if request.method == "POST":
        title = request.POST.get("title")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        tag = request.POST.get("tags")        
        summary = request.POST.get("summary")        
        content = request.POST.get("content")
        author = Author.objects.values_list("email_address")
        author = [i[0] for i in author]
        if email not in author:
            a = Author()
            a.first_name = firstname
            a.last_name = lastname
            a.email_address = email
            a.save()
            
        Tags = Tag.objects.values_list("caption")
        Tags = [i[0] for i in Tags]
        print(Tags)
        if tag not in Tags:
            t = Tag()
            t.caption = tag
            t.save()
        p = Post()
        p.title = title
        p.excerpt = summary
        p.content = content
        # p.tags.add(tag, tag)
        name = firstname + " " + lastname
        print(name)
        # p.author.add(name)
        # p.save()
        
        
        
        return redirect( "add")