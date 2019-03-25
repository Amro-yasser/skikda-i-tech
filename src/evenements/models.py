from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    places_avalaible=models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events_details", kwargs={"id": self.id})
    
    
