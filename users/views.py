from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def homepage(request):
    return render(request, 'users/home.html')

def signupuser(request):
    """Creates a form for sign up."""
    if request.method == "GET":
        return render(request, 'users/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], 
                                            password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentuser')
            except IntegrityError:
                return render(request, 'users/signupuser.html', 
                          {'form':UserCreationForm(), 'error': 'Username is already taken'})
                
        else:
            return render(request, 'users/signupuser.html', 
                          {'form':UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == "GET":
        return render(request, 'users/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username or password does not match'})
        else:
            login(request, user)
            return redirect('currentuser')
    


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('homepage')

def currentuser(request):
    
    return render(request, 'users/currentuser.html')


