from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('login/', login_view , name = 'login'),
    path('logout/', logout_view , name = 'logout'),
    path('signup/', signup_view , name = 'signup'),
    path('password-reset/',
         CustomPasswordResetView.as_view(
             template_name='registration/password_reset_form.html'
         ),
         name='password_reset'),
     
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),
     
    path('reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
     
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]