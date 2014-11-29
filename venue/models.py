from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_name = 'name'
    def __str__(self):
        return self.venue_name
