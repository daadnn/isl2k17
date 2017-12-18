from django.conf.urls import url

from . import views
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^create', views.create, name='create'),
    url(r'^channel', views.channel, name='channel'),
]
