from django.forms import ModelForm, Form, fields
from .models import VirtualHost


class VirtualHostForm(ModelForm):
    class Meta:
        model = VirtualHost
        fields = '__all__'


class DeleteConfirmation(Form):
    confirm = fields.BooleanField(label="Are you sure?")
