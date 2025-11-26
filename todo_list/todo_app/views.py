from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import path
from .models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .middlewares import auth

# Create your views here.


@login_required
def home(request):
    tasks = Todo.objects.filter(user=request.user)   # filter(user=request.user) lets you see tasks only the current user has created
    return render(request, 'home.html', {'tasks':tasks})


# CRUD operations
@login_required
def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        desc = request.POST.get('description')
        last_date = request.POST.get('last_date')
        
        Todo.objects.create(
            task = task,
            description = desc,
            last_date = last_date,
            user = request.user
        )
        return redirect('home')
    return render(request, 'add_task.html')

def description(request, id):
    task = get_object_or_404(Todo, id=id)
    return render(request, 'description.html', {'task': task})

@login_required
def edit_task(request, id):
    task = get_object_or_404(Todo, id=id, user=request.user)
    
    if request.method == 'POST':
        task.task = request.POST.get('task')
        task.description = request.POST.get('description')
        task.last_date = request.POST.get('last_date')
        task.save()
        return redirect('home')
    return render(request, 'edit_task.html', {'task':task})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Todo, id=id, user=request.user)
    task.delete()
    return redirect('home')
    


# Authentication
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')   # already logged in
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')   # already logged in
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required 
def logout_view(request):
    logout(request)
    return redirect("login")