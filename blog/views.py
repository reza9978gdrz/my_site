from django.shortcuts import render
from django.http import HttpResponse
def blog_view(request):
    return render(request,'website/blog-home.html')
def blog_single(request):
    context = {"title":'bitcoin crashed!','content':'bitcoin was flying but now grounded as always','author':'reza gholi'}
    return render(request,'website/blog-single.html',context)
# Create your views here.
