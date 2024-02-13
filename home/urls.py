from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('loginpage',views.login_page,name="loginpage"),
    path('loginauth',views.login_auth,name="loginauth"),
    path('signin',views.signin,name="signin"),
    path('logout',views.logoutuser,name="logout"),
    path('homepage',views.homepage,name='homepage'),
    path('signinauth',views.signin_auth,name="signinauth"),
    path('profile',views.profile,name="profile"),
    path('detailpage',views.detailpage,name="detailpage")
]