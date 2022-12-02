from django.shortcuts import render
from appointments.models import Appointment
from appointments.permissions import IsBloodCenter
from appointments.serializers import (
    AppointmentSerializer,
    BloodCenterAppointmentSerializer,
    DonorAppointmentSerializer,
    RequestBloodSerializer as RBS
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentSerializer


class BloodCenterAppointments(ListAPIView, UpdateModelMixin):
    permission_classes = [IsAuthenticated, IsBloodCenter]
    serializer_class = BloodCenterAppointmentSerializer
    lookup_field = "blood_center"

    def get_queryset(self, *args, **kwargs):
        center_id = self.kwargs.get('blood_center', None)
        return Appointment.objects.filter(blood_center=center_id)

    def put(self, *args, **kwargs):
        return self.partial_update(self.request, *args, **kwargs)


class DonorsAppointments(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DonorAppointmentSerializer

    def get_queryset(self, *args, **kwargs):
        donor_id = self.kwargs.get('donor_id', None)
        return Appointment.objects.filter(donor=donor_id)


class RequestBlood(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        res  = RBS.create(user, data)

        return Response(res.data, status=status.HTTP_200_OK)


    def get(self, request):
        user = request.user
        res = RBS.details(user)

        return Response(res.data, status=status.HTTP_200_OK)
        



