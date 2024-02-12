from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
# from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')

def login_page(request):
    return render(request,'log.html')

def login_auth(request):
    if request.method =="POST":
        email= request.POST.get('email')
        password= request.POST.get('password')
        #check if user has correct credentials
        user = authenticate(request,email=email, password=password)
        if User is not None:
           # A backend authenticated the credentials
           login(request,user)
           return redirect('homepage')
        else:
           # No backend authenticated the credentials
           return render(request,'log.html')

def logoutuser(request):
     logout()
     return redirect('/')

def signin(request):
    return render(request,'sign.html')

def signin_auth(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password')
        password2=request.POST.get('confirm-password')

        if password1!=password2:
            return HttpResponse("Your password and conform password are not same!!!!")
        else:
          my_user=User.objects.create_user(username,email,password1)
          my_user.save()
          return redirect('loginpage')


def homepage(request):
    if request.user.is_anonymous:
        return redirect('loginpage')
    else:
        return render(request,'home.html')







    


