from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

# register
class UserForm(UserCreationForm):
  class meta:
    model = User
    fields = ['name', 'email', 'password1', 'password2']