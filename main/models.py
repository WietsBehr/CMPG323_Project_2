from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Photo(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    captured_date = models.DateTimeField()
    image = models.ImageField(upload_to="media/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  f'{self.user.username} Photo'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




