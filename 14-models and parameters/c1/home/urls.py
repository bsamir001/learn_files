from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('test/', test_view),
    path('test_template/', test_template_view)
]
