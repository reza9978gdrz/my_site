from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from blog.models import Post 
import datetime as dt
from django.db.models import F
def blog_view(request):
     posts = Post.objects.filter(published_date__lte = dt.date.today())
     
     Post.objects.all().update(count_view=F('count_view')+1)
     context = {'posts':posts}
     return render(request,'website/blog-home.html',context)

def blog_single(request):
    return render(request,'website/blog-single.html')

def test(request,pid):
    post = Post.objects.get(id = pid)
    context = {'post':post}
    return render(request,"website/test.html",context)
# Create your views here.
