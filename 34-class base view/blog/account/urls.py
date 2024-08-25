from django.urls import path
from .views import *

app_name = "account"

urlpatterns = [
    path('register/', register_view, name="register"),
    path('test/', TestView.as_view(), name="test")

]