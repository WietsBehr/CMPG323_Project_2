from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Photo(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    captured_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="media/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

