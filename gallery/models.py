from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    



