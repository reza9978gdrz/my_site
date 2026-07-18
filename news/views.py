from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , redirect
from blog.models import Post 
from news.models import Contact , NewsLetter
from news.form import  ContactForm , NewsLetterForm
from django.contrib import messages
def home(request):
    return render(request,"website/index.html")

def about(request):
    return render(request,"website/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.name = 'anonymous'
            if obj.subject == '':
                obj.subject = None
            obj.save()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('news:contact')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def test(request):
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponse('thanks')
       else:
           return HttpResponse('not valid!')
    form = ContactForm()   
    return render(request,"website/test.html",{'form':form})

def newsletter(request):
    if request.method == "POST":
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
# Create your views here.
