from rest_framework import serializers

from .models import Appointment



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class BloodCenterAppointmentSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(required=False)
    date = serializers.DateField(required=False)
    class Meta:
        model = Appointment
        fields = [
            'id',
            'reason_for_decline',
            'donor',
            'phone',
            'blood_center',
            'status',
            'date',
            'time',
            'timestamp',
        ]
        read_only_fields = [
            'donor',
            'phone',
            'blood_center',
            'timestamp',
            'id'
        ]
        # depth = 1


class DonorAppointmentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Appointment
            exclude =  [
                'reason_for_decline',
                'blood_center',
            ]
