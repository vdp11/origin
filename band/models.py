

# Create your models here.
from django.db import models

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
