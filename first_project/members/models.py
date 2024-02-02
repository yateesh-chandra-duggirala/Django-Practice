from django.db import models
from django.utils import timezone

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null = True)
    entry_Date = models.DateField(default = timezone.now, null = True)