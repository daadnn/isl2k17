from django.conf.urls import url

from . import views
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^create', views.create, name='create'),
    url(r'^channel', views.channel, name='channel'),
    url(r'^new_message', views.new_message, name='new_message'),
    url(r'^fetch', views.fetch, name='fetch'),
]
