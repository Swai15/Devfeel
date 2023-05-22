from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post


# # register
# class UserForm(UserCreationForm):
#   class meta:
#     model = User
#     fields = ['name', 'email', 'password1', 'password2']

class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['name', 'email', 'password1', 'password2']
    labels = {
      'name' : 'Username'
    }

class CreatePostForm(forms.ModelForm):
  # body = forms.CharField(widget=CKEditorWidget)
  class Meta:
    model = Post
    fields = '__all__'
    exclude = ['author', 'likes']

class editProfileForm(forms.ModelForm):
  class Meta:
    model = User
    fields = {'name', 'email', 'bio', 'avatar'}

