#from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

# Create your views here.
longitude = 101
latitude = 20

user_location = fromstr(f"POINT({longitude} {latitude})", srid=4326)

class Home(ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:8]
    template_name = 'gisapp/index.html'
