from blog.views import *
from django.urls import path
app_name = 'blog'
urlpatterns = [
    path('', blog_view , name = 'index'),
    path('post-<int:pid>',blog_single , name = 'single'),
    #path('post-<int:pid>',test , name = 'test')
]