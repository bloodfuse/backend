import uuid
from django.db import models

T = True
F = False
# Create your models here.


class AnonymousVisitors(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    useragent = models.CharField(max_length=500, blank=T)
    fingerprint = models.CharField(max_length=150, blank=T)
    browser = models.CharField(max_length=150, blank=T)
    browser_type = models.CharField(max_length=150, blank=T)
    desktop = models.BooleanField(default=F)
    desktop_device = models.CharField(max_length=150, blank=T)
    desktop_device_type = models.CharField(max_length=150, blank=T)
    mobile = models.BooleanField(default=F)
    mobile_device = models.CharField(max_length=150, blank=T)
    mobile_device_type = models.CharField(max_length=150, blank=T)
    ip = models.CharField(max_length=150, blank=T)
    vpn = models.BooleanField(default=F)
    location = models.CharField(max_length=150, blank=T)
    language = models.CharField(max_length=150, blank=T)
    created = models.DateTimeField(auto_now_add=T)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.uuid}  anonymous visit info'
