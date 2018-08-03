import subprocess


def obtain_cert(vhost, test=False):
    subprocess.call(
        "certbot certonly --test-cert" +  # left --test-cert for now
        " --agree-tos --no-verify-ssl -n --webroot --webroot-path /var/www/" +
        vhost.domain_name + " -d " + vhost.domain_name
    )


def delete_cert(vhost):
    pass
