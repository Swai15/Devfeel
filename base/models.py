from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Create your models here.

class User(AbstractUser):
  name = models.CharField(max_length=200, null=True)
  email = models.EmailField(unique=True, null=True)
  bio = models.TextField(blank=True ,null=True)
  failed_login_attempts = models.IntegerField(default=0)
  # avatar = models.ImageField(null=True,default=)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through='Like', related_name='liked_posts')
    

    def __str__(self):
      return self.topic


class Like(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  like_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_commennts')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
  content = models.TextField()
  comment_date = models.DateTimeField(auto_now_add=True)