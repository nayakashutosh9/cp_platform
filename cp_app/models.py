from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Author(models.Model):
    name=models.CharField(max_length=100)
    author_pic=models.ImageField(upload_to='author_pics',blank=False)

class Problem(models.Model):
    title = models.CharField(max_length=200)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,related_name='tags')
    author = models.ManyToManyField(Author)

    description=models.CharField(max_length=10000)
    rating=models.PositiveIntegerField()
    link=models.URLField(max_length=100)
    def __str__(self):
        return self.title;
