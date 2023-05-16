from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, CreatePostForm
from django.utils.html import strip_tags
from .models import User, Post, Like, Comment


# Create your views here.


def home(request):
  posts = Post.objects.all()

  context = {'posts': posts}

  return render(request, 'base/home.html', context)


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
    return render(request, 'base/login_form.html', context)


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
  return render(request, 'base/register_form.html', context)

@login_required(login_url='login')
def createPost(request):
    form = CreatePostForm()
    if request.method == 'POST':
      form = CreatePostForm(request.POST)
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      return redirect('home')      

    context = {'form': form}
    return render(request, 'base/createpost_form.html', context)

def expandPost(request, pk):
  post = Post.objects.get(id=pk)

  context = {'post': post}
  return render(request, 'base/expand_post.html', context)

@login_required(login_url='login')
def updatePost(request, pk):
  post = Post.objects.get(id=pk)
  form = CreatePostForm(instance=post)
  if request.method == 'POST':
    form = CreatePostForm(request.POST, instance=post)

  if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
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

    return render(request, 'base/delete_post.html')


def userProfile(request, pk):
  user = User.objects.get(id=pk)
  posts = Post.objects.filter(author=user)

  context = {'user':user, 'posts':posts}
  return render(request, 'base/user_profile.html', context)

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

@login_required(login_url='login')
def submitComment(request, post_id):
  if request.method == 'POST':
    post = Post.objects.get(pk=post_id)
    comment_text = request.POST.get('comment-text')
    print(comment_text)
    comment = Comment.objects.create(post=post, user=request.user, content=comment_text)

    response = {
      'success': True,
      'comment': {
          'text': comment.content,
          'author': comment.user.name
      }
    }
  else:
      response = {'success': False}

  return JsonResponse(response)

