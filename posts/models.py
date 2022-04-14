from tabnanny import verbose
from turtle import title
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.core.signals import request_finished

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    post = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, related_name="post_likes", null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users_likes', null=True, on_delete=models.SET_NULL)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created']      
    
    def __str__(self):
        return "{} - {}".format(self.post.title, self.user.username)

class Dislike(models.Model):
    post = models.ForeignKey(Post, related_name="post_dislikes", null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users_dislikes', null=True, on_delete=models.SET_NULL)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return "{} - {}".format(self.post.title, self.user.username)