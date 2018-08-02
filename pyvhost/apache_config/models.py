from django.db import models


class VirtualHost(models.Model):

    def __str__(self):
        return self.domain_name

    domain_name = models.CharField(max_length=100)
    include_www = models.BooleanField(default=True)
    redirect_https = models.BooleanField(default=False)
    lets_encrypt = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    ssl_cert = models.TextField(blank=True)
    ssl_key = models.TextField(blank=True)
    ssl_bundle = models.TextField(blank=True)