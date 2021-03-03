from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class Glucose_tracker(models.Model):
    date = models.DateField()
    time = models.TimeField()
    glucose_number = models.CharField(max_length=4)
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    def commit(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.date) + ' ' + str(self.time)