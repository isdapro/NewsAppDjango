from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    location = models.CharField(max_length=50, default='us')
    empid = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Tasks(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.task_title
