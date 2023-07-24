from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.shortcuts import resolve_url
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from django.contrib import messages
from .forms import RegisterForm, CreatePostForm, editProfileForm
from django.utils.html import strip_tags
from .models import User, Post, Like, Comment

from django.core.files import File
from django.conf import settings
import os

User = get_user_model()
# Create your views here.


def home(request):
  search_posts = request.GET.get('search')

  if search_posts:
    posts = Post.objects.filter(Q(topic__icontains=search_posts) | Q(author__username__icontains=search_posts)).order_by('-post_date')
  else:
    posts = Post.objects.all().order_by('-post_date')

  paginator = Paginator(posts, 9)

  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)

  context = { 'page_obj':page_obj}

  return render(request, 'base/index.html', context)




def loginPage(request):
    if request.user.is_authenticated:
      return redirect('home')

    reset_password = False

    if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')

      user = authenticate(request,email=email, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        if User.objects.filter(email=email).exists():
          user = User.objects.get(email=email)
          user.failed_login_attempts += 1
          user.save()

          if user.failed_login_attempts >=1:
              token_generator = default_token_generator
              uid = user.pk
              token = token_generator.make_token(user)

              # Get the password reset URL
              reset_url = reverse('password_reset')
              reset_url = reset_url.replace('password_reset', '')
              reset_url = resolve_url(reset_url)

              reset_url += f'reset/{uid}/{token}/'
              reset_password = True
          messages.error(request, 'The password does not match the email')

        else:
          messages.error(request, 'The email is not registered with us')  
          reset_password = False  

    else:
      reset_password = False  

    context = {'reset_password': reset_password}
    return render(request, 'base/login_form.html', context)


def logoutPage(request):
  logout(request)
  return redirect('home')


def registerUser(request):
  form = RegisterForm()
  user = User
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
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
  return render(request, 'base/register_form.html', context)

@login_required(login_url='login')
def createPost(request):
    form = CreatePostForm()
    if request.method == 'POST':
      form = CreatePostForm(request.POST, request.FILES)
      if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('home')      
      else:
        print(form.errors)
        
    context = {'form': form}
    return render(request, 'base/createpost_form.html', context)

def expandPost(request, pk):
  post = Post.objects.get(id=pk)  
  post_comments = post.post_comments.all()

  if request.method == 'POST': 
    comment = Comment.objects.create(
      post=post,
      user=request.user,
      content=request.POST.get('comment-text')
      )

    return redirect('post-details', pk=post.id)

  context = {'post': post, 'post_comments': post_comments}
  return render(request, 'base/expand_post.html', context)

@login_required(login_url='login')
def updatePost(request, pk):
  post = Post.objects.get(id=pk)
  form = CreatePostForm(instance=post)
  if request.method == 'POST':
    form = CreatePostForm(request.POST, request.FILES, instance=post)

  if form.is_valid():
    if 'remove_post_image' in request.POST:
      post.post_image.delete()
      post.post_image =  'default_images/post_default.jpg'
    post.save()
    return redirect('post-details', pk=post.id)
    

  context = {'form':form}
  return render(request, 'base/updatepost_form.html', context)

@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
      post.delete()
      return redirect('home')

    return render(request, 'base/delete_post.html', {'post': post})


def userProfile(request, pk):
  user = User.objects.get(id=pk)
  search_post = request.GET.get('search')

  if search_post:
    all_posts = Post.objects.filter(author=user)
    posts = all_posts.filter(Q(topic__icontains=search_post))
  else:
    posts = Post.objects.filter(author=user)

  context = {'user':user, 'posts':posts}
  return render(request, 'base/user_profile.html', context)

@login_required(login_url='login')
def editUserProfile(request, pk):
  user = User.objects.get(id=pk)
  form = editProfileForm(instance=user)

  if request.method == 'POST':
    form = editProfileForm(request.POST,request.FILES,instance=user)
    if form.is_valid():
      if 'remove_avatar' in request.POST:
        user.avatar.delete()
        user.avatar = 'default_images/avatar.svg'
      form.save()
      return redirect('user-profile', pk=pk)

  context = {'user':user, 'form': form}
  return render(request, 'base/edit_user_profile.html', context)


def likePost(request, post_id):
    try:
      post = Post.objects.get(pk=post_id)
      like, created = Like.objects.get_or_create(user=request.user, post=post)
      if created:
        action = 'like'
      else: 
        like.delete()
        action = 'unlike'

      response = {'success': True, 'action':action}
    except Post.DoesNotExist:
      response = {'success': False, 'error': 'Post not found'}

    return JsonResponse(response)

def deleteComment(request, comment_id):
  comment = Comment.objects.get(pk=comment_id)
  if request.method == 'POST':
    comment.delete()
    return redirect('post-details', pk=comment.post.id)

  context = {'comment': comment}
  return render(request, 'base/delete_comment.html', context)

