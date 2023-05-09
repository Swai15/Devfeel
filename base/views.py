from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

