from django.shortcuts import render , redirect
from django.contrib.auth import  login , logout
from django.contrib.auth.forms import AuthenticationForm 
from .forms import  signup_form 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView , PasswordResetConfirmView 
from django.urls import reverse_lazy

UserModel = get_user_model()

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                    user = form.get_user()
                    login(request,user)
                    messages.success(request, f'congratulation {request.user.username}. you sign up successfully.')
                    return redirect('/')
            else:
                    messages.error(request, 'Invalid form submission.')
                    messages.error(request, "password or username or email was not true")
        
        else:
            form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html', context)
    else:
        return redirect('/')
         
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = signup_form(request.POST)
            if form.is_valid():
                user = form.save()
                login(request ,user)
                messages.success(request, 'congratulation you sign up successfully.')
                return redirect('/')
            else:
                messages.error(request, 'Invalid form submission.')
                messages.error(request, form.errors)
                return redirect('accounts:login')
            
        else:
            form = signup_form()
        context = {'form':form}
        return render(request,'accounts/signup.html', context)
    
    else:
        return redirect('/')

class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('accounts:password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('accounts:password_reset_complete')
     

# Create your views here.
