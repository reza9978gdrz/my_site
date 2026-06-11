from news.views import home,contact,about
from django.urls import path
urlpatterns = [
    path('', home),
    path('contact',contact),
    path('about',about)
]