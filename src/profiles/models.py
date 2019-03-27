from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField()
    email = models.EmailField()
    
