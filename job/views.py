from django.shortcuts import render
from django.shortcuts import render,redirect

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'job/register.html', {'form': form})

def index(request):
    return render(request,'job/index.html')

#def map(request):
 #   return render(request,'job/map.html')

def about(request):
    return render(request,'job/about.html')

def login_s(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(email,password)
            user = authenticate(request,email=email,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'User not exist')
                return redirect('login')
    else:
        form=LoginForm()
    return render(request,'job/login_s.html',{'form':form})

def signup(request):
    return render(request,'job/sign.html')