from django.template.loader import render_to_string

def gen_vhost(vhost):
    return render_to_string("vhost.txt", {"vhost": vhost})
