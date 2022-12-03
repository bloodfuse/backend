from uuid import uuid4
from django.db import models

from core.models import User


class Appointment(models.Model):
    STATUS = [
        ('pending', 'pending'),
        ('declined', 'declined'),
        ('accepted', 'accepted')
    ]

    id = models.UUIDField(unique=True, primary_key=True,
                          editable=False, default=uuid4)
    phone = models.CharField(max_length=15)
    time = models.TimeField()
    date = models.DateField()
    donor = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='donor')
    blood_center = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='blood_center')
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


class RequestsBlood(models.Model):
    BLOOD_TYPE = [
        ('nil', 'nil'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ]
    GENDER = [
        ('nil', 'nil'),
        ('male', 'male'),
        ('female', 'female')
    ]
    id = models.UUIDField(unique=True, primary_key=True,
                          editable=False, default=uuid4)
    username = models.CharField(max_length=255)
    blood_type = models.CharField(
        max_length=10, choices=BLOOD_TYPE, default=BLOOD_TYPE[0])
    gender = models.CharField(max_length=10, choices=GENDER, default=GENDER[0])
    center = models.CharField(max_length=255, blank=False)
    telephone = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        if self.completed:
            return self.username + ' Requested blood. -> [completed]'
        else:
            return self.username + ' Requested blood. -> [not completed]'
