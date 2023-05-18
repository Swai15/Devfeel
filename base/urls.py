from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.loginPage, name='login'),
  path('logout/', views.logoutPage, name='logout'),
  path('register/', views.registerUser, name='register'),
  path('create-post/', views.createPost, name='create-post'),  
  path('post-detail/<str:pk>/', views.expandPost, name='post-details'), 
  path('update-post/<str:pk>/', views.updatePost, name='update-post'),
  path('delete-post/<str:pk>/', views.deletePost, name='delete-post'),
  path('user-profile/<str:pk>/', views.userProfile, name='user-profile'),
  path('like-post/<int:post_id>/', views.likePost, name='like-post'),
  path('delete-comment/<str:comment_id>/', views.deleteComment, name='delete-comment'),
  path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
  path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
  path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]