from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    desc = models.CharField(max_length=256)

def __str__(self):
    return self.name
