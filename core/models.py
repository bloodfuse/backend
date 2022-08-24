from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ACCOUNT_TYPE = [
        ("donor", "donor"),
        ("recipient", "recipient"),
        ("admin", "admin"),
    ]

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
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP, blank=True)
    rc_number = models.CharField(max_length=15, blank=True)
    first_name = models.CharField(max_length=100, help_text='first_name')
    last_name = models.CharField(max_length=100, help_text='last_name')
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return f"{self.username} | last login: {self.last_login}"


class Notification(models.Model):
    pass


class Stat(models.Model):
    pass
