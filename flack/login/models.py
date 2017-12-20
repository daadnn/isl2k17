# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
# Create your models here.


def __str__(self):
    return self.user.username


# Crea perfil. Para que ande el registro del SuperUser, comentar todo el
# bloque a partir de aqui

