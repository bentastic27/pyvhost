from django.shortcuts import render, get_object_or_404, resolve_url
from ..models import VirtualHost
from ..config_functions import apache_vhost


def show(request, vhost_id):
    vhost = get_object_or_404(VirtualHost, pk=vhost_id)
    delete_url = resolve_url('apache_config:delete', vhost_id=vhost.id)
    listing_url = resolve_url('apache_config:listing')
    rendered_vhost = apache_vhost.gen_vhost(vhost)

    return render(
        request,
        'apache_config/show.html',
        {
            'vhost': vhost,
            'rendered_vhost': rendered_vhost,
            'delete_url': delete_url,
            'listing_url': listing_url
        }
    )
