from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.template import loader

# Create your views here.
def say_hello(request):
    return render(request, 'index.html')

def services_tab(request):
    return render(request, 'services.html')

def loginPage(request):
    return render(request, 'accounts/login.html')

def registerPage(request):
    form = UserCreationForm()
    context = {"form": form}
    return render(request, 'accounts/register.html')