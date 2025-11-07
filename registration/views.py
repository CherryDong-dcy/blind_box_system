from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout  # 添加logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm


def home(request):
    """首页"""
    return render(request, 'registration/home.html')


def register_view(request):
    """用户注册视图"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '注册成功！欢迎来到盲盒社交系统！')
            return redirect('home')
        else:
            messages.error(request, '注册失败，请检查表单信息！')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    """用户登录视图"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'欢迎回来，{username}！')
                return redirect('home')
            else:
                messages.error(request, '用户名或密码错误！')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    """自定义退出视图"""
    logout(request)
    messages.success(request, '您已成功退出！')
    return redirect('home')


@login_required
def profile_view(request):
    """用户个人资料页面"""
    return render(request, 'registration/profile.html', {'user': request.user})