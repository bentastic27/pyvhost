from django.shortcuts import render


def list(request):
    return render(request, 'apache_config/index.html')
