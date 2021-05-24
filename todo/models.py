from django.db import models
from django.utils import timezone
 
 # Class to hold all the details of the task
class Task(models.Model):
    title = models.CharField(max_length = 75, unique=True)
    description = models.TextField(null=True)
    date = models.DateTimeField(default = timezone.now)
    deadline = models.DateTimeField(default= timezone.now)
 
    def __str__(self):
        return self.title
# Create your models here.
