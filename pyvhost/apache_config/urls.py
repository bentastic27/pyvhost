from django.urls import path

from .views.index import index
from .views.create import create
from .views.list import list
from .views.delete import delete
from .views.show import show

urlpatterns = [
    path('', index, name='index'),
    path('list', list, name='list'),
    path('create', create, name='create'),
    path('show', show, name='show'),
    path('delete', delete, name='delete')
]
