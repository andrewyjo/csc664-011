from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Event'
        
class EventHierarchy(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'EventHierarchy'

class EventItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey(Event, models.DO_NOTHING)
    file = models.ForeignKey('File', models.DO_NOTHING)

    class Meta:
        db_table = 'Event_items'
        unique_together = (('event', 'file'),)


class File(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    filesize = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    coordinates = models.CharField(max_length=100, blank=True, null=True)
    tags = TaggableManager(blank=True)
    event = models.ForeignKey(Event, blank=True, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 'File'



class Library(models.Model):
    name = models.CharField(max_length=64, default=None)
    path = models.CharField(
        max_length=2048, default=None)

    class Meta:
        db_table = 'Library'

