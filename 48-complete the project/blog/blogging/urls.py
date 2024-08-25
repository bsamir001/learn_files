from django.urls import path
from .views import *

app_name = "blogging"

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
]
