from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:success_page')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form' : form})