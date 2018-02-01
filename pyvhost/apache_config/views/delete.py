from django.shortcuts import render


def delete(request):
    return render(request, 'apache_config/index.html')
