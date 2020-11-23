from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(name='Cairo')
        self.location.save_location()
 



      