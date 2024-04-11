from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model

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


def signup(request):
    # 1. POST 요청의 경우
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == "POST" :
        form = CustomUserCreationForm(request.POST)

        # 제공했던 회원가입 폼에 요청보낸 데이터를 포함하여, 그것이 유효한 데이터인 경우 저장한다.
        if form.is_valid():
            user = form.save()
            # 회원가입 후 바로 로그인 하는 경우
            auth_login(request,user)
            return redirect('articles:index')
    # 2. GET 요청 
    # 사용자가 회원가입 페이지에 들어서는 경우, 데이터를 입력할 form을 렌더링한다. 
    # django가 기존에 제공하는 UserCreationForm의 경우 model도 기본 UserModel을 사용하고 있고, 
    # 우리는 그 모델을 수정했기 때문에 UserCreationForm 또한 수정하여 사용해야 한다. 

    form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    # Templates Does Not Exists : render하는 경우에 파일 경로가 잘못된 경우 발생하는 에러
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



def profile(request, username):
    # get_user_model로 유저 모델의 직접참조를 피한다.
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request,user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)

    if person != request.user :
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else :
            person.followers.add(request.user)

    return redirect('accounts:profile', person.username)
