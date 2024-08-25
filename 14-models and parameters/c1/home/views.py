from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test_view(request):
    return HttpResponse("hello world")


def test_template_view(request):
    content = {'message': 'hello world', 'message2': 'Hi'}
    return render(request, 'home/test.html', content)


