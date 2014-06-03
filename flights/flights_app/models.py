from django.db import models

# Create your models here.
class Airport(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    IATA_code = models.CharField(max_length=4)
    ICAO_code = models.CharField(max_length=4, null=True)
    lat = models.FloatField()
    lon = models.FloatField()
    alt = models.IntegerField()
    timezone = models.FloatField()
    DST = models.CharField(max_length=1)

class Route(models.Model):
    airline_code = models.CharField(max_length=4)
    airline_id = models.IntegerField(null=True)
    source_code = models.CharField(max_length=4)
    source_id = models.IntegerField(null=True)
    dest_code = models.CharField(max_length=4)
    dest_id = models.IntegerField(null=True)
    codeshare = models.CharField(max_length=1)
    stops = models.IntegerField()
    equipment = models.CharField(max_length=100)
