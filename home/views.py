from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    return render(request,'index.html')


@login_required(login_url='/loginpage')
def homepage(request):
        context = {
            'posts': Post.objects.all()
        }
        return render(request,'home.html',context)

class PostListView(ListView):
    model = Post
    template_name= 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

# home/post_list.html
class PostDetailView(DetailView):
    model = Post
 

@login_required(login_url='/loginpage')
def detailpage(request):
    return render(request,'detail.html')

def logoutuser(request):
     logout(request)
     return redirect('/')






    


