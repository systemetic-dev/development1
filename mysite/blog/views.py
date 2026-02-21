from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.shortcuts import redirect
from .forms import PostForm
from django.urls import reverse

def hello(request):
    data = {
        "name": "Dev",
        "age": 20,
        "is_logged_in": True,
        "fruits": ["Apple", "Banana", "Mango"]
    }
    return render(request,'blog/hello.html',data)

def post_list(request):
    posts = Post.objects.all()
    # return render(request, 'blog/post_list.html', {"posts": posts})
    return redirect("blog:post_list")

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/posts/")
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {"form": form})