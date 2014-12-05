from django.contrib.gis.db import models
from django.contrib.gis import admin



class RawRequest(models.Model):
    Channel = models.CharField(max_length=75)
    Start_Date = models.CharField(max_length=50)
    End_Date = models.CharField(max_length=50)
    Metrics = models.CharField(max_length=100)
    Dimensions = models.CharField(max_length=100)
    Filters = models.CharField(max_length=100)
    Max_Results = models.CharField(max_length=50)
    Sort = models.CharField(max_length=50)
    Start_Index = models.CharField(max_length=50)
    Fields = models.CharField(max_length=50)

    Status = models.CharField(max_length=25, default='Submitted')

    def __unicode__(self):
        return self.Channel


class UserInput(models.Model):
    user = models.CharField("User name", max_length=50)
    following = models.IntegerField("Following ", blank=True)
    address = models.IntegerField("Point address", blank=True)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return "{}".format(self.name)


admin.site.register(UserInput, admin.OSMGeoAdmin)