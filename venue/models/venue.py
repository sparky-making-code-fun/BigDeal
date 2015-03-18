from django.db import models

# Create your models here.
class Venue(models.Model):
    venue_name = models.CharField(max_length=128)
    street = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.venue_name

    class Meta:
        managed = True
