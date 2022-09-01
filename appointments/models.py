from uuid import uuid4
from django.db import models

from core.models import User



class Appointment(models.Model):
    STATUS = [
        ('pending', 'pending'),
        ('declined', 'declined'),
        ('accepted', 'accepted')
    ]

    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid4)
    phone = models.CharField(max_length=15)
    time = models.TimeField()
    date = models.DateField()
    donor = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='donor')
    blood_center = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='blood_center')
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS[0])
    reason_for_decline = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Donor:  {0} | Center: {1}".format(
            self.donor,
            self.recipient
        )


class DonationHistory(models.Model):
    pass

    def __str__(self) -> str:
        return super().__str__()