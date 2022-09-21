from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from reports.models import Report



@receiver(post_save, sender=User)
def create_reports(instance, created, *args, **kwargs):
    if created and instance.account_type == 'donor':
        Report.objects.create(donor=instance)


