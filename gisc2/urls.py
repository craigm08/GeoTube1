from django.conf.urls import patterns, include, url
from django.contrib import admin
from GeoTube.views import *

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

    url(r'raw/$', RawView.as_view()),
    url(r'map/$', MapView.as_view()),
    url(r'graph/$', GraphView.as_view()),

    url(r'^accounts/', include('registration.backends.simple.urls')),
)
