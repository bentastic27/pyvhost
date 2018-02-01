from django.shortcuts import render


def show(request):
    return render(request, 'apache_config/index.html')
