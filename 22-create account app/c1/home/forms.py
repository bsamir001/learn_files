from django import forms
from .models import Customer


class CustomerForm(forms.Form):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    phone = forms.CharField(label='Phone')
    country = forms.CharField(label='Country')
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(label='ege')
    city = forms.CharField(label='City')


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'country', 'email', 'age', 'city']
