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
            'role',
            'last_name',
            'rc_number',
            'center_name',
            'location',
            'gender',
            'phone',
            'password1',
            'password2'
        ]
        extra_kwargs = {
            # 'password1': {'write_only': True},
            'password1': {'write_only': True},
        }

    @transaction.atomic
    def save(self, request, *args, **kwargs):
        data = self.data
        user = super().save(request)
        user.username = data.get('email')
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')
        user.phone = data.get('phone')
        user.fullname = f"{ data.get('first_name') }_{ data.get('last_name') }"
        user.email = data.get('email')
        user.blood_group = data.get('blood_group', '')
        user.location = data.get('location', '')
        user.gender = data.get('gender', '')
        user.rc_number = data.get('rc_number', '')
        user.center_name = data.get('center_name', '')
        user.account_type = data.get('account_type')
        user.save()
        return user


class UserLoginSerializer(LoginSerializer):
    ACCOUNT_TYPE = [
        ("donor", "donor"),
        ("donation_center", "donation_center"),
        ("empty", "empty"),
    ]

    GENDER = [
        ("male", "Male"),
        ("female", "Female"),
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
    gender = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
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
            'role',
            'rc_number',
            'phone',
            'gender',
            'location',
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
            'role',
            'gender',
            'location',
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
            'role',
            'rc_number',
            'phone',
            'gender',
            'location',
            'blood_group',
            'account_type',
            'center_name'
        ]
        depth = 1

    def details(user, level='user'):
        y = User.objects.filter(username=str(user))
        if not y.exists():
            y = User.objects.filter(email=str(user))
        val = {
            'message': 'failed',
            'data': 'No data found'
        }
        if level == 'user':

            if y.exists():
                roles = []
                for z in y:
                    if z.role == 5133:
                        roles.append(5133)
                        roles.append(4758)
                        roles.append(3214)
                        roles.append(2033)
                        roles.append(1155)
                    elif z.role == 4758:
                        roles.append(4758)
                        roles.append(3214)
                        roles.append(2033)
                        roles.append(1155)
                    elif z.role == 3214:
                        roles.append(3214)
                        roles.append(2033)
                        roles.append(1155)
                    elif z.role == 2033:
                        roles.append(2033)
                        roles.append(1155)
                    elif z.role == 1155:
                        roles.append(1155)
                    xval = {
                        'email': z.email,
                        'first_name': z.first_name,
                        'last_name': z.last_name,
                        'id': z.id,
                        'role': roles,
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
        else:
            if y.exists():
                roles = []
                for z in y:
                    if z.role == 5133:
                        roles.append(5133)
                        roles.append(4758)
                        roles.append(3214)
                        roles.append(2033)
                        roles.append(1155)
                    elif z.role == 4758:
                        roles.append(4758)
                        roles.append(3214)
                        roles.append(2033)
                        roles.append(1155)
                    elif z.role == 3214:
                        roles.append(3214)
                        roles.append(2033)
                        roles.append(1155)
                    elif z.role == 2033:
                        roles.append(2033)
                        roles.append(1155)
                    elif z.role == 1155:
                        roles.append(1155)
                    xval = {
                        'email': z.email,
                        'id': z.id,
                        'role': roles,
                    }
                val = {
                    'message': 'success',
                    'data': xval
                }

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
            'location',
            'gender',
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
