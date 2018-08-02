import os
import subprocess
from django.template.loader import render_to_string
from django.conf import settings


def gen_vhost(vhost):
    return render_to_string("apache_config/vhost.txt", {"vhost": vhost})


def write_vhost(vhost):
    vhost_file_path = settings.APACHE_VHOST_DIR + "/"
    vhost_file_path += vhost.domain_name + ".conf"

    if os.path.isdir(settings.APACHE_VHOST_DIR):
        vhost_file = open(vhost_file_path, 'w')
        vhost_file.write(gen_vhost(vhost))
        vhost_file.close()
    else:
        return False

    reload_apache()
    return True


def delete_vhost(vhost):
    vhost_file_path = settings.APACHE_VHOST_DIR + "/"
    vhost_file_path += vhost.domain_name + ".conf"

    if os.path.exists(vhost_file_path):
        os.remove(vhost_file_path)
    else:
        return False
    
    reload_apache()
    return True


def reload_apache():
    subprocess.call(["systemctl", "reload", "apache2"])
    return True


def restart_apache():
    subprocess.call(["systemctl", "restart", "apache2"])
    return True
