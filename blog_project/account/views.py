from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error' : 'invalid login'})
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')