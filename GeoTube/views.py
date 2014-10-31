from django.shortcuts import render
from django.views import generic

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "index.html"

class WhoView(generic.TemplateView):
    template_name = "who.html"

class WhatView(generic.TemplateView):
    template_name = "what.html"

class WhyView(generic.TemplateView):
    template_name = "why.html"

class RawView(generic.TemplateView):
    template_name = "raw.html"

class MapView(generic.TemplateView):
    template_name = "map.html"

class GraphView(generic.TemplateView):
    template_name = "graph.html"
