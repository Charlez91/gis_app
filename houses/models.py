from django.contrib.gis.db import models as gis_models
from django.db import models

# Create your models here.
class House(models.Model):
    number = models.CharField(max_length=100, null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    #owner = gis_models.CharField(null=True, blank= True)
    location = gis_models.PointField(srid=4326,null=True, blank=True)

    def __str__(self) -> str:
        return f"house {self.number} with {self.bedrooms} bedrooms"
