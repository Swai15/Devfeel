from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from django.utils.html import strip_tags


# Create your views here.


def home(request):

  return render(request, 'base/home.html', {})


def loginPage(request):
    if request.user.is_authenticated:
      return redirect('home')

    if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')

      user = authenticate(request,email=email, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        messages.error(request, 'Usermame or password does not exist')

    context = {}
    return render(request, 'base/login.html', context)


def logoutPage(request):
  logout(request)
  return redirect('home')


def registerUser(request):
  form = RegisterForm()
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.name = user.name.lower()
      user.save()
      login(request, user)
      return redirect('home')
    else:
      errors = form.errors
      error_messages = []
      for field in errors:
        for error in errors[field]:
          error_messages.append(error)
      messages.error(request, ' '.join(error_messages))

  context = {'form': form}
  return render(request, 'base/register.html', context)
