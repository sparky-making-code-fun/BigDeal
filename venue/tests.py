from django.test import TestCase
from models.venue import Venue


class TestVenue(TestCase):
    """Test our venue class"""

    def test_make_venue(self):
        """Can we even make a venue?"""

        v = Venue.objects.create(venue_name='Howdy', street='12')
        self.assertEqual(v.venue_name, 'Howdy')
        self.assertEqual(v.street, '12')
