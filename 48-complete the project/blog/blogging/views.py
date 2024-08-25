from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.contrib import messages


# Create your views here.

class HomePageView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, "blogging/home_page.html", context={'posts': posts})


class CreatePostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blogging/create_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "پست شما با موفقیت ایجا شد.")
            return redirect("blogging:home_page")
        return render(request, 'blogging/create_post.html', {'form': form})


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, "blogging/post_detail.html", {"post": post})
