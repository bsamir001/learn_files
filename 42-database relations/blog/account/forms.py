from django import forms
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
