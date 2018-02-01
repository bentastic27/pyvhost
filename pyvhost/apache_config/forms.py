from django.forms import ModelForm
from .models import VirtualHost


class VirtualHostForm(ModelForm):
    class Meta:
        model = VirtualHost
        fields = '__all__'
