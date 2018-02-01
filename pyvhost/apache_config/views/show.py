from django.shortcuts import render, get_object_or_404
from ..models import VirtualHost


def show(request, vhost_id):
    vhost = get_object_or_404(VirtualHost, pk=vhost_id)
    return render(request, 'apache_config/show.html', {'vhost': vhost})
