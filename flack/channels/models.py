# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#from login.models import User
from organizations.models import Organization

from django.contrib.auth.models import User

class Channel(models.Model):
    """
    Channel Model
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)    
    channel = models.CharField(null=False, max_length=100, blank=False)
    thematic = models.CharField(null=False, max_length=100, blank=False)

    def __unicode__(self):
        return self.channel


class Message(models.Model):
    """
    Message Model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    message = models.CharField(null=False, max_length=300, blank=False)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.message
