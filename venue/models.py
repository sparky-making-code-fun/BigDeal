from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_name = models.CharField(max_length=128)
    def __str__(self):
        return self.venue_name
