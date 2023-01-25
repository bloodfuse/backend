from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ACCOUNT_TYPE = [
        ("donor", "donor"),
        ("donation_center", "donation_center"),
        ("empty", "empty"),
    ]

    GENDER = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    ROLES = [
        (5133, "admin"),
        (4758, 'editor'),
        (3214, 'customer service'),
        (2033, 'low staff'),
        (1155, 'end user'),
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

    id = models.UUIDField(unique=True, primary_key=True,
                          editable=False, default=uuid4)
    role = models.BigIntegerField(choices=ROLES, default=1155)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    blood_group = models.CharField(
        max_length=3, choices=BLOOD_GROUP, blank=True)
    rc_number = models.CharField(max_length=15, blank=True)
    first_name = models.CharField(
        max_length=100, help_text='first_name', blank=True)
    last_name = models.CharField(
        max_length=100, help_text='last_name', blank=True)
    center_name = models.CharField(
        max_length=500, help_text='Name of hospital, center or blood bank', blank=True)
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=300)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    email = models.EmailField(max_length=255, unique=True)
    email_is_verified = models.BooleanField(default=False)
    # otp = models.CharField(max_length=6, blank=True, editable=False)
    # otp_is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username


class Notification(models.Model):
    pass


class Stat(models.Model):
    pass
