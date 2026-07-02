from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post 
def home(request):
    return render(request,"website/index.html")
def about(request):
    return render(request,"website/about.html")
def contact(request):
    return render(request,"website/contact.html")

# Create your views here.
