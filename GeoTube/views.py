from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, UpdateView
from models import *
from forms import *
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.gis.geos import Point

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "GeoTube/index.html"

class WhoView(generic.TemplateView):
    template_name = "GeoTube/who.html"

class WhatView(generic.TemplateView):
    template_name = "GeoTube/what.html"

class WhyView(generic.TemplateView):
    template_name = "GeoTube/why.html"

class MapView(generic.TemplateView):
    template_name = "GeoTube/map.html"

class GraphView(generic.TemplateView):
    template_name = "GeoTube/graph.html"

class SampleView(generic.TemplateView):
    template_name = "GeoTube/sample.html"

class UserInputView(generic.edit.CreateView):
    model = UserInput
    form_class = MyGeoForm
    template_name = 'GeoTube/map.html'
    success_url = reverse_lazy("main_page")

