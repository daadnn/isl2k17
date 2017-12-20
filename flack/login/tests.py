# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.test import TestCase

from django.contrib.auth.models import User

from django.db import IntegrityError

from .forms import (
    UserForm,
    EditUserForm,
)

class QuestionTestCase(TestCase):

    def create_user(self):
        user = User.objects.create(username="prueba1",
                                email="prueba1@prueba.com",
                                password = "1234qwer")
        return user

    def test_repeated_username(self):
        user = User.objects.create(username="prueba1",
               email="prueba1@prueba.com", password = "1234qwer")
        try:
            user2 = User.objects.create(username="prueba1",
                    email="prueba1@prueba.com", password = "1234qwer")
            created = True
        except IntegrityError:
            created = False

        self.assertFalse(created)

    def test_empty_username_form(self):
        data = {'username': "", 'password': "1234qwer",'email': "a@a.com"}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())

    def test_incorrect_pass_form(self):
        data = {'username': "malafama", 'password': "123456",'email': "a@a.com"}
        form = UserForm(data=data)
        self.assertFalse(form.is_valid())
