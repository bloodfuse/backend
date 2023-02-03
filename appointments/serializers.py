from core.utils import send_sms
from rest_framework import serializers

from .models import Appointment, RequestsBlood as RB

from core.models import User


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

        def update(self, instance, validated_data):
            instance.reason_for_decline = validated_data.get(
                'reason_for_decline',
                instance.reason_for_decline
            )
            instance.date = validated_data.get(
                'date',
                instance.date
            )
            instance.time = validated_data.get(
                'time',
                instance.time
            )

            if validated_data.get('data') or validated_data.get('time'):
                sms_message = """ 
                Dear {firstname}, 
                \n \nYour appointment with {blood_center} been rescheduled to {date} by {time}.
                \n \nThanks for your understanding. 
                """.format(
                    firstname=instance.donor.first_name,
                    blood_center=instance.blood_center,
                    date=instance.date,
                    time=instance.time
                )
                send_sms(instance.phone, sms_message)
            return instance


class DonorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        exclude = [
            'reason_for_decline',
            'blood_center',
        ]

    def all(center_id):
        xList = []
        data = {}
        try:
            # print(type(center_id))
            # y = User.objects.get(username=center_id[0])
            app = Appointment.objects.filter(blood_center_id=center_id.id)
            for x in app:
                res = {
                    "donor": f"{x.donor.first_name} {x.donor.last_name}",
                    "date": x.date,
                    "time": x.time,
                    "approval":  str(x.approval),
                    "status": x.status,
                    "id": str(x.id)
                }
                xList.append(res)

            class Response(object):
                data = {}
                data['data'] = xList
                data['status'] = 200
                data = data

        except Exception as e:

            class Response(object):
                data = {}
                data['error'] = str(e)
                data['status'] = 500
                data = data

        return Response

    def appointments(donor_id):
        xList = []
        data = {}
        try:
            # print(type(center_id))
            # y = User.objects.get(username=donor_id[0])
            app = Appointment.objects.filter(donor=donor_id)
            for x in app:
                res = {
                    "centerName": f"{x.blood_center.center_name}",
                    "date": x.date,
                    "time": x.time,
                    "approval":  str(x.approval),
                    "status": x.status,
                    "id": str(x.id)
                }
                xList.append(res)

            class Response(object):
                data = {}
                data['data'] = xList
                data['status'] = 200
                data = data

        except Exception as e:

            class Response(object):
                data = {}
                data['error'] = str(e)
                data['status'] = 500
                data = data

        return Response


class RequestBloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RB
        fields = ['username']

    def create(user, data):
        try:
            # y = User.objects.get(username=user[0])
            x = RB()
            x.username = str(user),
            x.blood_type = data['blood_type'],
            x.gender = data['gender'],
            x.center = data['center'],
            x.telephone = data['telephone']
            x.save()

            class Response(object):
                data = {'message': 'Created successfully'}

        except Exception as e:
            class Response(object):
                data = {'message': 'Error occurred',
                        'error': str(e),
                        }

        return Response

    def details(user):
        xLists = []
        # user = User.objects.get(username=str(user))

        getRequests = RB.objects.filter(username=user)
        if getRequests.exists():
            for i in getRequests:
                val = {
                    'id': i.id,
                    'user': i.username.username,
                    'blood_type': i.blood_type,
                    'gender': i.gender,
                    'center': i.center,
                    'telephone': i.telephone,
                    'completed': i.completed,
                }
                xLists.append(val)

            class Response(object):
                data = xLists
        else:
            class Response(object):
                data = xLists

        return Response
