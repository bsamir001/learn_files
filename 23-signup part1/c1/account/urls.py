from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('signup/', signup_view, name='signup')
]
