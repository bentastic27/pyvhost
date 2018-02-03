from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ..models import VirtualHost
from ..forms import VirtualHostForm


def create(request):
    create_form = VirtualHostForm(request.POST or None)

    if request.method == 'POST' and create_form.is_valid():
        new_vhost = VirtualHost(
            domain_name=create_form.cleaned_data['domain_name'],
            include_www=create_form.cleaned_data['include_www'],
            redirect_https=create_form.cleaned_data['redirect_https'],
            php_enabled=create_form.cleaned_data['php_enabled'],
            lets_encrypt=create_form.cleaned_data['lets_encrypt'],
            active=create_form.cleaned_data['active']
        )
        new_vhost.save()
        return HttpResponseRedirect(
            reverse('apache_config:show', kwargs={
                'vhost_id': new_vhost.id
            })
        )

    return render(
        request,
        'apache_config/create.html',
        {'create_form': create_form}
    )