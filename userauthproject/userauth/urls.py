from django.conf.urls import patterns, include, url
from django.contrib import admin
from userauth import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name="index"),
	url(r'^register/', views.register, name="register"),
	url(r'^login/', views.user_login, name="login"),
	url(r'^logout/', views.user_logout, name="logout"),
	url(r'^profile/', views.showprofile, name="showprofile"),
)