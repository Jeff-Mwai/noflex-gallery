from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Location, Category

# Create your views here.
def images(request):
    pictures = Image.objects.all()
    location = Location.objects.all()
    return render(request, 'index.html', {'pictures':pictures, 'location':location})