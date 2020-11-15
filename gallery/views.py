from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Location, Category

# Create your views here.
def images(request):
    pictures = Image.objects.all()
    location = Location.objects.all()
    return render(request, 'index.html', {'pictures':pictures, 'location':location})

def search_image(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})

def location(request, location):
    images_by_location = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images_by_location})