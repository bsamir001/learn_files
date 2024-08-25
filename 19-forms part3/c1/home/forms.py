from django import forms


class CustomerForm(forms.Form):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    phone = forms.CharField(label='Phone')
    country = forms.CharField(label='Country')
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(label='ege')
    city = forms.CharField(label='City')
