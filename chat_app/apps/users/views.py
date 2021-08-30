from django.shortcuts import render, redirect
from django.contrib.auth import login

from apps.users.forms import RegisterForm, LogInForm
from apps.users.models import CustomUser

def login_user(request):
    user_form = LogInForm()
    if request.method == 'POST':
        user_form = LogInForm(request.POST)
        if user_form.is_valid():
            login(request, CustomUser.objects.get(username=request.POST['username']), backend='django.contrib.auth.backends.ModelBackend')
            return redirect('chat/jobsity/')
    return render(request, 'login.html', {'form' : user_form})

def register(request):
    user_form = RegisterForm()
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('chat/jobsity/')
    return render(request, 'register.html', {'form' : user_form})