from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.loginPage, name='login'),
  path('logout/', views.logoutPage, name='logout'),
  path('register/', views.registerUser, name='register'),
  path('create-post/', views.createPost, name='create-post'),  
]