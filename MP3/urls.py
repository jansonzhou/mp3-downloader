"""MP3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
=======
#from MP3.home import views
>>>>>>> ac0de343d9e4f9324a9182ec958ce0a2f1e31e5b
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^downloads/', include('downloads.urls')),
    url(r'^accounts/', include('User.urls')),
<<<<<<< HEAD
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^home', views.home, name='home'),
    url(r'^temp', views.temp, name='temp'),
=======
   # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^$', views.home,name='home'),
>>>>>>> ac0de343d9e4f9324a9182ec958ce0a2f1e31e5b
]
