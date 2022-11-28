from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    items = models.ManyToManyField(
        'File',
        related_name='File'
    )
    startTime = models.DateTimeField(blank=True, null=True)
    endTime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'Event'

    

    


class File(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    filesize = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    tags = TaggableManager(blank=True)

    class Meta:
        db_table = 'File'



class Library(models.Model):
    name = models.CharField(max_length=64, default=None)
    path = models.CharField(
        max_length=2048, default=None)

    class Meta:
        db_table = 'Library'


