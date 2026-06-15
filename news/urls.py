from news.views import home , about ,contact
from django.urls import path
app_name = 'news'
urlpatterns = [
    path('', home , name = 'index'),
    path('about',about, name = 'about'),
    path('contact',contact, name = 'contact')
]