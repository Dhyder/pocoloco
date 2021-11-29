from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Location, Category, Editor

# Create your views here.
def gallery(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    return render(request, 'gallery.html', {"images":images, "locations":locations})
