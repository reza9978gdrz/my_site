from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from blog.models import Post 
import datetime as dt
from django.db.models import F
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def blog_view(request,cat_name=None, author_name=None):
     posts =Post.objects.filter(status = 1)
     if cat_name:
        posts = posts.filter(category__name = cat_name)
     elif author_name:
        posts = posts.filter(author__username = author_name)
     else:
         posts = Post.objects.filter(published_date__lte = dt.date.today())

     posts = Paginator(posts,3)
     page_number = request.GET.get('page')
     try:
        posts = posts.get_page(page_number)
     except PageNotAnInteger:
         posts = posts.page(1)
     except EmptyPage:
         posts = posts.page(1)
     context = {'posts':posts}
     return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    prev_post = None
    next_post = None
    post =get_object_or_404(Post , id = pid , status = 1)
    post_list =list(Post.objects.filter(status = 1))
    post_index = post_list.index(post)
    if post_index > 0 :
        prev_post = post_list[post_index-1]
    if post_index < len(post_list)-1:
        next_post = post_list[post_index+1]
    #post = Post.objects.update(count_view=F('count_view')+1)
    # it will be slightly different in your computer
    post.count_view = post.count_view + 1
    post.save()
    context = {'post':post , 'prev_post':prev_post , 'next_post':next_post}
    return render(request,'blog/blog-single.html',context)

def test(request):
    return render(request,"website/test.html")
# Create your views here.

def blog_search(request):
    posts =Post.objects.filter(status = 1)
    if request.method == 'GET':
       if s:= request.GET.get('s'):
            posts = posts.filter(content__contains= s)
    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
