from django.urls import path
from .views import *

app_name = "blogging"

urlpatterns = [
    path("home_page/", HomePageView.as_view(), name="home_page"),
]
