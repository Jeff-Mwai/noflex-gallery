from django.db import models

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

    def save_location(self):
        self.save()

    @classmethod
    def get_locations(cls):
        locations = cls.objects.all()
        return locations

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', default = 'images.jpg')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)


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
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()









