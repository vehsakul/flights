from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'flights.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'airports/location', airport_location),
    url(r'airports/autocomplete', airport_autocomplete),
)

