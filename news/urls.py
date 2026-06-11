from news.views import home,news,about
from django.urls import path
urlpatterns = [
    path('', home),
    path('news',news),
    path('about',about)
]