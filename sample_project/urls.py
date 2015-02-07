from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('sample_app.urls')),
    url(r'^another_app/$', include('another_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
