from django.db import models


class Venue(models.Model):
    venue_name = 'name'
    def __str__(self):
        return self.venue_name
