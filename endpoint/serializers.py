from django.core import exceptions
from rest_framework import serializers

from .models import (
    AnonymousVisitors as AV
)

from core.models import User

T = True
F = False

from .utils import (ran_gen as RG)

class AnonymousVisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AV
        fields = ['uuid']

    def create(data):
        try:
            AV.create(
            useragent = data['useragent'],
            fingerprint = data['fingerprint'],
            browser = data['browser'],
            browser_type = data['browser_type'],
            desktop = data['desktop'],
            desktop_device = data['desktop_device'],
            desktop_device_type = data['desktop_device_type'],
            mobile = data['mobile'],
            mobile_device = data['mobile_device'],
            mobile_device_type = data['mobile_device_type'],
            ip = data['ip'],
            vpn = data['vpn'],
            location = data['location'],
            language = data['language'],
        )

            class Response(object):
                data = {}
                data["status"] = 201
                data = data

        except Exception as e:
            class Response(object):
                data = {}
                data["status"] = 500
                data["error"] = str(e)
                data = data
        
        return Response

    def read():
        try:
            xList = []
            getAllAnnon = AV.objects.all()

            for x in getAllAnnon:
                val = {
                    'useragent': x.useragent,
                    'fingerprint': x.fingerprint,
                    'browser': x.browser,
                    'browser_type': x.browser_type,
                    'desktop': x.desktop,
                    'desktop_device': x.desktop_device,
                    'desktop_device_type': x.desktop_device_type,
                    'mobile': x.mobile,
                    'mobile_device': x.mobile_device,
                    'mobile_device_type': x.mobile_device_type,
                    'ip': x.ip,
                    'vpn': x.vpn,
                    'location': x.location,
                    'language': x.language,
                }
                xList.append(val)

            class Response(object):
                data = {}
                data["status"] = 201
                data = data

        except Exception as e:
            class Response(object):
                data = {}
                data["status"] = 500
                data["error"] = str(e)
                data = data

        return Response


class AllDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid']

    def read():
        try: 
            xList = []
            getAllDonors = User.objects.filter(account_type='donor')
            for x in getAllDonors:
                val = {
                    
                        "uid": x.id,
                        # "image": x.image,
                        "image": None,
                        "name": x.fullname,
                        "gender": x.gender,
                        "location": x.location,
                        "phnNumb": x.phone,
                }
                xList.append(val)
                class Response(object):
                    data = {}
                    data["status"] = 200
                    data["results"] = xList
                    data = data

        except Exception as e:
            class Response(object):
                data = {}
                data["status"] = 500
                data["error"] = str(e)
                data = data

        return Response

            
            

