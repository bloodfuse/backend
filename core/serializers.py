from core.models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializers):
    class Meta:
        model = CustomUser
        fields = []