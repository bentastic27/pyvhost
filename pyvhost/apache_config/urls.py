from django.urls import path

from .views.index import index
from .views.create import create
from .views.list import listing
from .views.delete import delete
from .views.show import show

app_name = 'apache_config'

urlpatterns = [
    path('', index, name='index'),
    path('list/', listing, name='listing'),
    path('create/', create, name='create'),
    path('show/<int:vhost_id>/', show, name='show'),
    path('delete/<int:vhost_id>/', delete, name='delete')
]
