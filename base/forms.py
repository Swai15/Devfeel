from django import forms
from django.forms import ModelForm, FileInput, ImageField
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
  post_image = ImageField(widget=FileInput)
  
  class Meta:
    model = Post
    fields = ['topic', 'description', 'body', 'post_image']
    # exclude = ['author', 'likes']

class EditPostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    exclude = ['author', 'likes']

class editProfileForm(forms.ModelForm):
  avatar = ImageField(widget=FileInput)
  class Meta:
    model = User
    fields = {'name', 'email', 'bio', 'avatar'}

