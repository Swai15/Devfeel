from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

from .models import User, Post, Comment

class CustomUserAdmin(UserAdmin):
  list_display = ('id','name', 'email', 'avatar')

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)