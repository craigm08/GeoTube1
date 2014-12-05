from GeoTube.views import *
from django.contrib.gis import admin
admin.autodiscover()
from django.conf.urls import patterns, url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view()),
    url(r'home/', HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'who/$', WhoView.as_view()),
    url(r'what/$', WhatView.as_view()),
    url(r'why/$', WhyView.as_view()),

    url(r'map/$', MapView.as_view()),
    url(r'graph/$', GraphView.as_view()),
    url(r'sample/$', SampleView.as_view()),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
