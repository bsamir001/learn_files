from django.shortcuts import render, redirect
from .forms import *


# Create your views here.

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
