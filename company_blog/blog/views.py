from django.shortcuts import render
from django.contrib import messages
from blog.models import Post
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class PostListView(ListView):
    # template_name = 'home.html'
    context_object_name = 'posts'
    model = Post
    ordering = ['-date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class AboutView(TemplateView):
    template_name ='about.html'

class PostDetailView(DetailView):
    model = Post
#
class CreatePostView(LoginRequiredMixin,CreateView):
    model= Post
    fields = ['title','content']
    redirect_field_name = 'blog/post_detail.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
#
class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    redirect_field_name = 'blog/post_detail.html'
    model = Post
    fields = ['title','content']
    # success_url = reverse_lazy("blog:post_list")
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
#
#
class  DeletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    messages.success(request, 'You have Successfully logged in!')
