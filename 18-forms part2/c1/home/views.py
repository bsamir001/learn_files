from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm


# Create your views here.

def test_view(request):
    return HttpResponse("hello world")


def test_template_view(request):
    content = {'message': 'hello world', 'message2': 'Hi'}
    return render(request, 'home/test.html', content)


def show_customers_view(request):
    customers = Customer.objects.all()
    content = {'customers': customers}
    return render(request, 'home/show_customers.html', content)


def create_customer_view(request):
    if request.method == "GET":
        form = CustomerForm()
        return render(request, 'home/create_customer.html', {'form': form})
    else:
        pass
