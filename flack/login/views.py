# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect

from django.http import JsonResponse

import re


from .forms import (
    UserForm,
    EditUserForm,
)


def index(request):
    return render(request, "index.html")


# Register View
def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Guardar formulario
            form.save()
            # Una vez registrado, lo loguea
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return home(request)
        else:
            # si esta mal rellenado, se carga de nuevo registro
            return render(request, 'login/register.html', {'form': form})
    else:
        form = UserForm()
        args = {'form': form}
        return render(request, 'login/register.html', args)

# Edit User View
@login_required  # Requiere que este logueado
def edit_profile(request):
    if request.method == 'POST':
        # formulario enviado
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile/profile')
    else:
        # formulario inicial
        form = EditForm(instance=request.user)

        args = {'form': form}
        return render(request, 'profile/edit_profile.html', args)


@login_required
def home(request):
    # si el usuario es admin lo lleva a la pagina de admins
    user = request.user
    if user.is_superuser:
        return HttpResponseRedirect("/admin")
    # si no, lo lleva a home
    else:
        template = loader.get_template('home.html')
        context = {
        }
        return HttpResponse(template.render(context, request))


# Visualizar el profile
@login_required
def profile(request, pk=None):
    storage = messages.get_messages(request)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user, 'message': storage}
    return render(request, 'login/profile.html', args)



# See if the given username exists in the DB.
def validate_username(request):
    username = request.GET.get('username', None)
    flag = User.objects.filter(username__iexact=username).exists()
    data = {
        'is_taken': flag
    }
    return JsonResponse(data)


# See if the given pass is valid.
def validate_pass(request):
    pass1 = request.GET.get('pass', None)
    match1 = re.search("^.*[a-zA-Z]+.*$", pass1)
    match2 = re.search("^.*[0-9]+.*$", pass1)
    data = {
        'es_valido': match1 != None and match2 != None
    }
    return JsonResponse(data)

# See if the given username and pass corresponds with an existing account
def validate_password(request):
    pass1 = request.GET.get('password', None)
    username = request.GET.get('username', None)
    kwargs = {'username': username}
    user = User.objects.get(**kwargs)
    flag = user.check_password(pass1)
    data = {
        'match': flag
    }
    return JsonResponse(data)


def signout(request):
    logout(request)
    return render(request, "index.html")
