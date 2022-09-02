from django.shortcuts import render
from appointments.models import Appointment
from appointments.serializers import (
    AppointmentSerializer,
    BloodCenterAppointmentSerializer,
    DonorAppointmentSerializer
)

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AppointmentSerializer


class BloodCenterAppointments(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BloodCenterAppointmentSerializer

    def get_queryset(self, *args, **kwargs):
        center_id = self.kwargs.get('center_id', None)
        return Appointment.objects.filter(center=center_id)

    def put(self, *args, **kwargs):
        return self.partial_updates(self.request, *args, **kwargs)


class DonorsAppointments(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DonorAppointmentSerializer

    def get_queryset(self, *args, **kwargs):
        donor_id = self.kwargs.get('donor_id', None)
        return Appointment.objects.filter(donor=donor_id)

