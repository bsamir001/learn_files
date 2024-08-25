from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('test/', test_view),
    path('test_template/', test_template_view),
    path('show_customers/', show_customers_view, name='show_customers'),
]
