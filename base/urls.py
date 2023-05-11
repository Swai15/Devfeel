from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.loginPage, name='login'),
  path('logout/', views.logoutPage, name='logout'),
  path('register/', views.registerUser, name='register'),
  path('create-post/', views.createPost, name='create-post'),  
  path('post-detail/<str:pk>', views.expandPost, name='post-details'), 
  path('update-post/<str:pk>', views.updatePost, name='update-post'),
  path('delete-post/<str:pk>', views.deletePost, name='delete-post'),
  path('user-profile/<str:pk>', views.userProfile, name='user-profile')
]