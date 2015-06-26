from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'logout/$', views.logout),
    url(r'oauth2callback', views.auth_return, name='return'),
]