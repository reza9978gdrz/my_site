from django import template
import datetime as dt
from blog.models import Post,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

register = template.Library()

@register.simple_tag(name='totalpost')

def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def upper(value):
    return value.title.upper()

@register.filter
def snipett(value,arg=20 ):
    return value[:arg] + '...'

@register.inclusion_tag('website/popularpost.html')
def popular_posts():
    posts = Post.objects.filter(status=1).order_by('-count_view')[:3]
    return {'posts':posts} 

@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    category = Category.objects.all()
    cat_dict = {}
    for name in category:
        cat_dict[name] = posts.filter(category = name).count()
    return {'category':cat_dict}

@register.inclusion_tag('blog/blog-recent-post.html')
def recent_posts():
    posts = Post.objects.filter(status=1,published_date__lte = dt.date.today()).order_by('-published_date')[:6]
    return {'posts':posts}