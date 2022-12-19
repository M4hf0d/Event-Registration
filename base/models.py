from abc import update_abstractmethods
from asyncio import events
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100, null = True)
    email = models.EmailField(unique=True, null = True)
    bio = models.TextField(null = True, blank = True)
    participant = models.BooleanField(default=True, null = True)
    # avatar = models.ImageField(null = True, blank = True)

    USERNAME_FIELD = 'email'   # Auth with EmailField
    REQUIRED_FIELDS=['username']

class Event(models.Model):
    name = models.CharField(max_length  = 255)
    description = models.TextField(max_length =1000, null = True, blank = True)
    participants = models.ManyToManyField(User , blank = True, related_name = "events")
    date = models.DateTimeField()
    created = models.DateField(auto_now_add = True) #Create 
    updated  = models.DateField(auto_now = True) #Update

    def __str__ (self):
        return self.name

class Submission(models.Model):
    participant = models.ForeignKey(User, on_delete = models.SET_NULL , null = True , related_name="submission")
    event = models.ForeignKey(Event, on_delete = models.SET_NULL, null = True)
    details = models.TextField(max_length =255, null = True, blank = True)
    
    def __str__(self):
        return str(self.participant.name) + '-----' + str(self.event)
# str(self.participant.name)
