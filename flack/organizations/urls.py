from django.conf.urls import url

from . import views
from .views import *
from django.views.generic import TemplateView

# We are adding a URL called /home
urlpatterns = [
    url(r'^list', views.organizationlist, name='organizationlist'),
    url(r'^create', views.create, name='create'),
]
