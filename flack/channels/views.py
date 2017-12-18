
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

from organizations.models import Organization, OrganizationMember

from organizations.views import organization

from .models import Channel, Message

from django.contrib.auth.models import User

from .forms import (
    ChannelForm,
)

# Create your views here.


@login_required
def create(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save()
            organization_id = channel.organization_id
            return organization(request,organization_id)
    else:
        organization_id = request.GET.get('organization', None)
        args = {'user': request.user,
                'organization_id': organization_id
        }
        return render(request, 'channels/create.html', args)
        
@login_required
def channel(request):
    channel_id = request.GET.get('id', None)
    channel = get_object_or_404(Channel, pk=channel_id)
    
    user = request.user
    template = loader.get_template('channels/channel.html')
    context = {
        'user': request.user,
        'channel': channel
    }
    return HttpResponse(template.render(context, request))

