from django.shortcuts import render, redirect
from .models import User

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username, password=password)
        return redirect('home')
    return render(request, 'core/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            # Implement your login logic here
            return redirect('dashboard')
        else:
            # Handle invalid credentials
            pass
    return render(request, 'core/login.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

