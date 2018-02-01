from django.shortcuts import render, get_object_or_404
from ..models import VirtualHost
from ..forms import DeleteConfirmation


def delete(request, vhost_id):
    vhost = get_object_or_404(VirtualHost, pk=vhost_id)
    confirm_delete = DeleteConfirmation
    return render(
        request,
        'apache_config/delete.html',
        {
            'vhost': vhost,
            'confirm_delete': confirm_delete
        }
    )
