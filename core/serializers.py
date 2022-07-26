from uuid import uuid4
from django.contrib.auth.hashers import check_password, make_password
from django.db import transaction
from core.utils import get_random_string, send_sms
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer

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
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')
        user.phone = data.get('phone')
        user.fullname = f"{ data.get('first_name') }_{ data.get('last_name') }"
        user.email = data.get('email')
        user.blood_group = data.get('blood_group', '')
        user.rc_number = data.get('rc_number', '')
        user.center_name = data.get('center_name', '')
        user.account_type = data.get('account_type')
        user.save()
        return user


class UserLoginSerializer(LoginSerializer):
    ACCOUNT_TYPE = [
        ("donor", "donor"),
        ("donation_center", "donation_center"),
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

    id = serializers.UUIDField(default=uuid4)
    account_type = serializers.CharField(required=False)
    blood_group = serializers.CharField(required=False)
    rc_number = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    center_name = serializers.CharField(required=False)
    fullname = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    email = serializers.CharField(required=True)
    email_is_verified = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'id',
            'rc_number',
            'phone',
            'blood_group',
            'account_type',
            'center_name'
        ]
        read_only_fields = [
            'first_name',
            'last_name',
            'id',
            'rc_number',
            'phone',
            'blood_group',
            'account_type',
            'center_name'
        ]


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
            'center_name'
        ]
        depth = 1

    def details(user):
        y = User.objects.filter(username=str(user))
        val = {
            'message': 'failed',
            'data': 'No data found'
        }

        if y.exists():
            for z in y:
                xval = {
                    'email': z.email,
                    'first_name': z.first_name,
                    'last_name': z.last_name,
                    'id': z.id,
                    'rc_number': z.rc_number,
                    'phone': z.phone,
                    'blood_group': z.blood_group,
                    'account_type': z.account_type,
                    'center_name': z.center_name,
                }
            val = {
                'message': 'success',
                'data': xval
            }
        # val = {
        #     "user": str(user),
        #     "type": str(type(user))
        # }

        class Response(object):
            data = val

        return Response


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
            'rc_number',
            'account_type',
            'center_name',
        ]
