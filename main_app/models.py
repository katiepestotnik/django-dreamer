from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Goal(models.Model):
    name = models.CharField(max_length=100)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_weight = models.IntegerField()
    end_weight = models.IntegerField()
    exercise = ArrayField(models.CharField(max_length=100, blank=True))
    completed = models.BooleanField()
    
    def __str__(self):
        return self.name

  