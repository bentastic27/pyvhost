from django.shortcuts import render, get_object_or_404, resolve_url
from ..models import VirtualHost


def show(request, vhost_id):
    vhost = get_object_or_404(VirtualHost, pk=vhost_id)
    delete_url = resolve_url('apache_config:delete', vhost_id=vhost.id)
    return render(
        request,
        'apache_config/show.html',
        {
            'vhost': vhost,
            'delete_url': delete_url
        }
    )