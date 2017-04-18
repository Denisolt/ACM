from django.db import models
from colorfield.fields import ColorField
from django.utils import timezone
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def publish(self):
        self.save()
    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    desc = models.TextField()
    color = ColorField(default='#3498db')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

   

class Competition(models.Model):
    team = models.CharField(max_length=100)
    email = models.EmailField()
    member1 = models.CharField(max_length=50)
    member2 = models.CharField(max_length=50)
    member3 = models.CharField(max_length=50)
    file = models.FileField()
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.team
