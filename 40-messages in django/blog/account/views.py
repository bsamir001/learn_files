from django.shortcuts import render, redirect
from .forms import *
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("blogging:home_page")
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("blogging:home_page")
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "ثبت نام با موفقیت انجام شد.")
            return redirect('blogging:home_page')


class LoginView(View):
    def post(self, request):
        if request.user.is_authenticated:
            return redirect("blogging:home_page")
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "با موفقیت وارد شدید.")
                return redirect('blogging:home_page')
            else:
                messages.error(request, "نام کاربری یا رمز عبور اشتباه است")
        return render(request, 'account/login.html', {'form': form})

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("blogging:home_page")
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("blogging:home_page")
        logout(request)
        messages.success(request, "با موفقیت از حساب کاربری خود خارج شدید.")
        return redirect('blogging:home_page')
