from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('test/', test_view),
    path('test_template/', test_template_view),
    path('show_customers/', show_customers_view, name='show_customers'),
    path('create_customer/', create_customer_view),
    path('create_customer_model_form/', create_customer_model_view),
    path('success/', success_view, name='success_page')
]
