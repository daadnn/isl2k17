# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from datetime import *

from django.utils import timezone

from django.http import JsonResponse

from django.core.mail import send_mail

from .models import Organization, OrganizationMember

from channels.models import Channel

from django.contrib.auth.models import User

from .forms import (
    OrganizationForm,
)

# Create your views here.


@login_required
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
            organization = form.save()
            user = request.user
            om = OrganizationMember()
            om.organization = organization
            om.user = user
            om.save()
            return organizationlist(request)
    else:
        args = {'user': request.user
        }
        return render(request, 'organizations/create.html', args)


@login_required
def organization(request,organization_id='0'):
    # If organization_id is 0, it isn't a redirection so the organization_id
    # should be in the get parameter
    if organization_id == '0':
        organization_id = request.GET.get('id', None)
    organization = get_object_or_404(Organization, pk=organization_id)
    channels = Channel.objects.filter(organization=organization_id)
    
    user = request.user
    is_owner = organization.owner == user
    template = loader.get_template('organizations/organization.html')
    context = {
        'user': request.user,
        'organization': organization,
        'channels': channels,
        'is_owner': is_owner
    }
    return HttpResponse(template.render(context, request))

@login_required
def invite(request):
    # Set organization_id to 0 so I can check if I need the get 
    # parameter or if it comes by a post parameter
    organization_id = 0
    if request.method == 'POST':
        email = request.POST.get('email', None)
        organization_id = request.POST.get('organization', None)
        organization = get_object_or_404(Organization, pk=organization_id)        
        message = "You have been invited to form part of the organization " + \
                   organization.organization + ", if you want to join, just " + \
                   "follow the next <a href='localhost:8000/login/register?" + \
                   "organization=" + organization_id + "'>link</a>"
        
        send_mail(
            'You have been invited to '+ organization.organization,
            message,
            'flack@flack.com',
            [email],
        )
        success = True
    if organization_id == 0:
        organization_id = request.GET.get('organization', None)
        success = False
    args = {'organization': organization_id,
            'user': request.user,
            'success': success
    }
    return render(request, 'organizations/invite.html', args)

