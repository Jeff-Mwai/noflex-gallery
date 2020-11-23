from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,default='location')


    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__category_name__icontains=category)
        return images

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()










