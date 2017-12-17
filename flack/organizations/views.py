# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from datetime import *

from django.utils import timezone

from django.http import JsonResponse

from .models import Organization, OrganizationMember, OrganizationInvitation

from django.contrib.auth.models import User

from .forms import (
    OrganizationForm,
)

# Create your views here.


def organizationlist(request):
    user = request.user
    organizations = Organization.objects.filter(owner = user)
    template = loader.get_template('organizations/list.html')
    context = {
        'user': request.user,
        'organizations': organizations
    }
    return HttpResponse(template.render(context, request))


@login_required
def create(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return organizationlist(request)
    else:
        form = OrganizationForm()
        args = {'form': form,
                'user': request.user
        }
        return render(request, 'organizations/create.html', args)
