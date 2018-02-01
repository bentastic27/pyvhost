from django.shortcuts import render
from ..forms import VirtualHostForm


def create(request):
    create_form = VirtualHostForm
    return render(
        request,
        'apache_config/create.html',
        {'create_form': create_form}
    )
