from django.template.loader import render_to_string

def gen_vhost(vhost):
    return render_to_string("apache_config/vhost.txt", {"vhost": vhost})
