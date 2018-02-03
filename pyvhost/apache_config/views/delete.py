from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from ..models import VirtualHost
from ..forms import DeleteConfirmation


def delete(request, vhost_id):
    vhost = get_object_or_404(VirtualHost, pk=vhost_id)
    confirm_delete = DeleteConfirmation(request.POST or None)

    if request.method == 'POST' and confirm_delete.is_valid():
        if confirm_delete.cleaned_data['confirm']:
            vhost.delete()
            return HttpResponseRedirect(
                reverse('apache_config:listing')
            )

    return render(
        request,
        'apache_config/delete.html',
        {
            'vhost': vhost,
            'confirm_delete': confirm_delete
        }
    )
