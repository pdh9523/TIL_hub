from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 매서드가 POST 형식일 때 (로그인 과정)
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    # 매서드가 GET 형식일 때 (로그인 페이지 제공)
    form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

## GET 요청의 경우 페이지, POST 요청의 경우 회원가입 진행
## 구조적으로 create 함수와 동일하다.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST" :
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 바로 로그인 하는 경우
            auth_login(request,user)
            return redirect('articles:index')

    form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request) :
    # delete 하려는 유저 == request를 하는 유저(request.user)
    # 그래서, 삭제하려는 유저를 조회할 필요는 없다.
    request.user.delete()
    # 탈퇴 후 세션에 대해서도 삭제 시행
    auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    form = CustomUserChangeForm(instance=request.user)

    context = {
        'form' : form ,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request, user_pk):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
        # 패스워드 체인지 폼은 첫번째 user 인자가 필수.
    form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)