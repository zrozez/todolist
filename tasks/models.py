from django.db import models

# Create your models here.

class Task(models.Model):
    body = models.TextField()
    estimated_finish_time = models.DateTimeField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

