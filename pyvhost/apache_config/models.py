from django.db import models


class VirtualHost(models.Model):

    def __str__(self):
        return self.domain_name

    domain_name = models.CharField(max_length=100)
    include_www = models.BooleanField(default=True)
    redirect_https = models.BooleanField(default=True)
    php_enabled = models.BooleanField(default=False)
    lets_encrypt = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
