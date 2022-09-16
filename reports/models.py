from uuid import uuid4
from django.db import models

from core.models import User


class Reports(models.Model):

    BLOOD_GROUP = [
        ("O-", "O-"),
        ("O+", "O+"),
        ("A-", "A-"),
        ("A+", "A+"),
        ("B-", "B-"),
        ("B+", "B+"),
        ("AB-", "AB-"),
        ("AB+", "AB+"),
    ]

    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid4)
    donor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_donor')
    donation_center = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donation_center', blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP, blank=True)
    blood_count = models.PositiveIntegerField(default=0)
    weight = models.FloatField(default=0.0)
    blood_pressure =  models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    blood_donation_quantity = models.PositiveIntegerField(default=0)
    donation_time = models.TimeField()
    donation_date = models.DateField()
    timestamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Donor: {0} | Donation Center {1}".format(
            self.donor,
            self.donation_center
        )
