from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            # return redirect()
            return render(request, 'account/register.html', {'form': form})


class LoginView(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return redirect()
            else:
                form.add_error(None, "نام کاربری یا رمز عبوراشتباه است.")
        return render(request, 'account/login.html', {'form': form})

    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        #return redirect()

