from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.views import View


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            # return redirect()
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


class TestView(View):
    def get(self, request):
        return HttpResponse("hello user")

    def post(self, request):
        return HttpResponse("hi user")
