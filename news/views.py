from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"website/index.html")
def about(request):
    return render(request,"website/about.html")
def contact(request):
    return render(request,"website/contact.html")
def test(request):
    context = {'name':'reza' , 'last_name':'gholialigudarzi'}
    return render(request,"website/test.html",context)
# Create your views here.
