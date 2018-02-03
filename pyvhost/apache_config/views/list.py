from django.shortcuts import render, reverse
from ..models import VirtualHost


def listing(request):
    vhost_list = VirtualHost.objects.all()
    create_url = reverse('apache_config:create')
    return render(
        request,
        'apache_config/list.html',
        {'vhost_list': vhost_list, 'create_url': create_url}
    )
