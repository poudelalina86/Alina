from django.contrib import admin
# from home.models import Login

# Register your models here.
# admin.site.register(Login)
from .models import Post
from .models import PostComment

admin.site.register(Post)
admin.site.register(PostComment)