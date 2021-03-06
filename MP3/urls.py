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
from . import views
from cart.views import cart, checkout
from User.models import User
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^temp', views.temp, name='temp'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('User.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^home', views.home, name='home'),
    url(r'^temp', views.temp, name='temp'),
    url(r'^search/', views.search, name='search'),
    url(r'^cart/$', cart, name='cart'),
    url(r'^cart/checkout/$', checkout, name='checkout'),

    url(r'^', include('downloads.urls')),
    # url(r'^', include('cart.urls')),
    url(r'^oauth2/', include('oauth2.urls', namespace="oauth2")),

    url(r'^$', views.loginhome, name='loginhome'),
    # url(r'^', include(router.urls)),
]
