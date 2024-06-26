from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
def login(request):
    # 로그인 하려는 경우
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')

    # 로그인 페이지를 띄우려는 경우
    form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def signup(request):
    if request.method == "POST" :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
        
    form = CustomUserCreationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def update(request):
    if request.method == "POST" :
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
        
    form = CustomUserChangeForm(instance=request.user)

    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')

def change_password(request, user_pk):

    if request.method == "POST" :
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('movies:index')
        
    form = PasswordChangeForm(request.user)
    
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)