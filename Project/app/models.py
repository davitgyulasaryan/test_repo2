import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rate = models.FloatField(default=0.0)
    count = models.IntegerField(default=0)


class Lecture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

