from django.contrib import admin
# from home.models import Login

# Register your models here.
# admin.site.register(Login)
from .models import Post

admin.site.register(Post)
