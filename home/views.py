from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, PostComment
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def index(request):
    return render(request,'index.html')


@login_required(login_url='/loginpage')
def homepage(request):
        context = {
            'posts': Post.objects.all()
        }
        return render(request,'home.html',context)

# class PostListView(ListView):
#     model = Post
#     template_name= 'home.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Get all comments related to the posts
#         comments = PostComment.objects.select_related('post').filter(post__in=context['posts'])
#         context['comments'] = comments
#         return context

from .forms import CommentForm

class PostListView(ListView):
    model = Post
    template_name= 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all comments related to the posts
        comments = PostComment.objects.select_related('post').filter(post__in=context['posts'])
        context['comments'] = comments
        # Add comment form to the context
        context['comment_form'] = CommentForm()
        return context
    

# home/post_list.html
class PostDetailView(DetailView):
    model = Post
    template_name= 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # Add comment form to the context
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()  # Get the post associated with the comment
            comment = form.save(commit=False)
            comment.user = request.user  # Assuming the user is authenticated
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk) 
 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name= 'post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = 'homepage'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

def postComment(request, slug):
    if request.method=="POST":
     pass
    return redirect("homepage")

   


@login_required(login_url='/loginpage')
def detailpage(request):
    return render(request,'detail.html')

def logoutuser(request):
     logout(request)
     return redirect('/')






    


