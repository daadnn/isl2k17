from django.conf.urls import url

from . import views
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^list', views.organizationlist, name='organizationlist'),
    url(r'^create', views.create, name='create'),
    url(r'^organization', views.organization, name='organization'),
    url(r'^invite', views.invite, name='invite'),
    url(r'^join', views.join, name='join'),
]
