from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin#A subclass of geomodeladmin but supports open street map which gives a better detailed map dan
from .models import Shop

# Register your models here.
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
