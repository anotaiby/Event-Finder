from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default='None')
    desc = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    time = models.DateTimeField('time')
    image = models.ImageField(upload_to='media')
