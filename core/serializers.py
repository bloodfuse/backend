from uuid import uuid4
from django.contrib.auth.hashers import check_password, make_password
from django.db import transaction
from core.utils import get_random_string, send_sms
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from core.models import User


class UserRegisterSerializer(RegisterSerializer, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'blood_group',
            'account_type',
            'first_name',
            'last_name',
            'rc_number',
            'center_name',
            'phone',
            'password1',
            'password2'
        ]
        extra_kwargs = {
            'password1': {'write_only': True},
            'password1': {'write_only': True},
        }

    @transaction.atomic
    def save(self, request, *args, **kwargs):
        data = self.data
        user = super().save(request)
        user.username = "{0}_{1}_{2}".format(
            data.get('first_name'),
            data.get('last_name'),
            get_random_string(6)
        ),
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.phone = data.get('phone')
        user.fullname = f"{ data.get('first_name') }_{ data.get('last_name') }"
        user.email = data.get('email')
        user.blood_group = data.get('blood_group', '')
        user.rc_number = data.get('rc_number', '')
        user.center_name = data.get('center_name', '')
        user.account_type = data.get('account_type')
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'id',
            'rc_number',
            'phone',
            'blood_group',
            'account_type',
        ]
        depth = 1


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'account_type'
        ]


class BloodCentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'rc_number',
            'account_type'
        ]
