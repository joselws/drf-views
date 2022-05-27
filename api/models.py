from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    active = models.BooleanField()
    school = models.CharField(max_length=100)