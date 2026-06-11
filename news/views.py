from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("سلام! این اولین اپ من است.")
def about(request):
    return HttpResponse("this is about us")
def news(request):
    return HttpResponse("<h1>there is no news here</h1>")
# Create your views here.
