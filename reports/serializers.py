import requests
from core.utils import send_sms

from .models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = [
            'donation_center',
            "blood_group",
            "blood_count",
            "weight",
            "blood_pressure",
            "age",
            "blood_donation_quantity",
            "donation_time",
            "donation_date",
            "timestamp",
        ]


class CenterReportSerializer(serializers.ModelSerializer):
    donation_time = serializers.TimeField(required=False)
    donation_date = serializers.DateField(required=False)
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = [
            'donor',
            'donation_center',
            'age',
            'timestamp',
        ]
        # depth = 1

        def update(self, instance, validated_data):
            instance.weight = validated_data.get(
                'weight',
                instance.weight
            )
            instance.blood_count = validated_data.get(
                'blood_count',
                instance.blood_count
            )
            instance.blood_pressure = validated_data.get(
                'blood_pressure',
                instance.blood_pressure
            )
            instance.blood_donation_quantity = validated_data.get(
                'blood_donation_quantity',
                instance.blood_donation_quantity
            )


            sms_message = """ 
            Dear {firstname}, 
            \n \n we sincerely appreciate your effort in taking out time to donate {blood_quantify}pints of your blood to save a live. \n
            A medical report will be created for you soon, while you wait 
            You will be paid some incentives shortly kindly check your dashboard.
            \n \n
            Thanks you.
            """.format(
                firstname       =   instance.donor.firstname,
                blood_quantify  =   instance.blood_donation_quantity
            )
            send_sms(instance.phone, sms_message)
            return instance
