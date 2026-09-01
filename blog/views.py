from django.shortcuts import render

#Printing anything using HttpResponse
#from django.http import HttpResponse

def home(request):
    return render(request, 'blog/index.html')
