from django.contrib.gis import forms
from views import RawRequest
from models import *


class RawRequestForm(forms.ModelForm):
    class Meta:
        model = RawRequest
        fields = ('Channel', 'Start_Date', 'End_Date', 'Metrics',
                  'Dimensions', 'Filters', 'Max_Results', 'Sort', 'Start_Index', 'Fields')


class MyGeoForm(forms.Form):
    geom = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    user = forms.CharField(max_length=50, required=True)
    following = forms.CharField(max_length=50, required=True)
    address = forms.CharField(max_length=50, required=True)
