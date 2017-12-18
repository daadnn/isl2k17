# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from login.models import User


class Organization(models.Model):
    """
    Organization Model
    """
    
    organization = models.CharField(null=False, max_length=100, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.organization


class OrganizationMember(models.Model):
    """
    Organization X User Model
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.answer
