from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plate = models.TextField()
    sensors = models.TextField()
    file_skye = models.FileField(upload_to='uploads/')
    file_ino = models.FileField(upload_to='uploads/')
