from django.shortcuts import render


def index(request):
    return render(request, 'apache_config/index.html')
