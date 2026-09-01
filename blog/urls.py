from django.urls import path
from . import views

urlpatterns = [
    # Path for homepage of the blog
    path('', views.home, name='blog-home'),
]
