from django.db import models
from django.contrib.auth.models import User

class Attraction(models.Model):
    name = models.CharField(max_length= 32)
    description = models.TextField(max_length= 360, default= None)
    location = models.CharField(max_length= 100)

class Event(models.Model):
    name = models.CharField(max_length= 32)
    description = models.TextField(max_length= 360, default= None)
    startTime = models.DateTimeField(auto_now= False, auto_now_add= False)
    endTime = models.DateTimeField(auto_now= False, auto_now_add= False)
    location = models.CharField(max_length= 100)

class Outing(models.Model):
    name = models.CharField(max_length= 32)
    description = models.TextField(max_length= 360, default= None)
    date = models.DateField(auto_now= False, auto_now_add= False)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    events = models.ManyToManyField(Event)


