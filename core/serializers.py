from uuid import uuid4
from django.contrib.auth.hashers import check_password, make_password
from django.db import transaction
from core.utils import get_random_string
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from core.models import User



class UserRegisterSerializer(RegisterSerializer, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'blood_group', 'account_type', 'rc_number', 'fullname', 'password1', 'password2']

    @transaction.atomic
    def save(self, request, *args, **kwargs):
        data = self.data
        user = super().save(request)
        user.username = "{0}_{1}".format(data.get('fullname'), get_random_string(5)),
        user.fullname = data.get('fullname')
        user.email = data.get('email')
        user.blood_group = data.get('blood_group', '')
        user.rc_number = data.get('rc_number', '')
        user.account_type=data.get('account_type')
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = [
            'email',
            'fullname',
            'id',
            'rc_number',
            'blood_group',
            'account_type',
        ]
        depth = 1
