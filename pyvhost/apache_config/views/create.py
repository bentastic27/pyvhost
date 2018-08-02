from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ..models import VirtualHost
from ..forms import VirtualHostForm
from ..config_functions.apache_vhost import write_vhost


def create(request):
    create_form = VirtualHostForm(request.POST or None)

    if request.method == 'POST' and create_form.is_valid():
        new_vhost = VirtualHost(
            domain_name=create_form.cleaned_data['domain_name'],
            include_www=create_form.cleaned_data['include_www'],
            redirect_https=create_form.cleaned_data['redirect_https'],
            lets_encrypt=create_form.cleaned_data['lets_encrypt'],
            active=create_form.cleaned_data['active'],
            ssl_cert=create_form.cleaned_data['ssl_cert'],
            ssl_key=create_form.cleaned_data['ssl_key'],
            ssl_bundle=create_form.cleaned_data['ssl_bundle']
        )
        new_vhost.save()
        
        if new_vhost.active:
            write_vhost(new_vhost)

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