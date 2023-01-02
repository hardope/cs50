from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User')
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, related_name='User')
    text = models.CharField(max_length=400, null=False)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f'{self.user} posts at {self.date}'


class Comment(models.Model):
    comment = models.TextField(null=False)
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented in {self.post}'


class Profile(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    follower = models.ManyToManyField(User, blank=True, related_name="follower")
    following = models.ManyToManyField(User, blank=True, related_name="following")

    def __str__(self):
        return f'{self.user}'
