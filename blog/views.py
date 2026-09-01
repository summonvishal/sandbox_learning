from django.shortcuts import render

#Home page
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to my website!!!</h1>")
