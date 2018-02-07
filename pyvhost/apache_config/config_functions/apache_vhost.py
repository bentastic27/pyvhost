from django.template import Context
from .misc import get_template


def gen_vhost(vhost):
    return get_template("vhost.txt").render(Context({"vhost": vhost}))
