from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from tinymce import HTMLField

User = get_user_model()

class Moderator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField()




class Event(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    places_avalaible=models.IntegerField(default=0)
    description =models.TextField()
    chapitre=models.TextField()
    moderators = models.ManyToManyField(Moderator)
    
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events_details", kwargs={"id": self.id})
    
    
