from django.conf.urls import patterns, include, url
from django.conf import settings

from userauth import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('userauth.urls')),
)
