from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post
from .forms import PostForm


#Printing anything using HttpResponse
#from django.http import HttpResponse

@login_required
def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the logged-in user as author
            post.save()
            return redirect('blog-home')
    else:
        form = PostForm()

    posts = Post.objects.all()  # Retrieve all blog posts from DB
    return render(request, 'blog/index.html', {'posts': posts, 'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in automatically after signup
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
