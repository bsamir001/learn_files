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
        form = CustomerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone = form.cleaned_data["phone"]
            country = form.cleaned_data["country"]
            email = form.cleaned_data["email"]
            age = form.cleaned_data["age"]
            city = form.cleaned_data["city"]
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                country=country,
                email=email,
                age=age,
                city=city
            )
            customer.save()
            return HttpResponse("موفقیت آمیز")
        return HttpResponse("ناموفق. لطفا دوباره تلاش کنید.")
