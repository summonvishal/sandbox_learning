from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#Printing anything using HttpResponse
#from django.http import HttpResponse

def home(request):
    return render(request, 'blog/index.html')

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
