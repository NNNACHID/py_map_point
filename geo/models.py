from django.contrib.gis.db import models


class PointOfInterest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.PointField(srid=4326)  

    def __str__(self):
        return self.name
