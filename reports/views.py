from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.decorators import action

from .permissions import centerIsPermitted, isPermittedDonor
from .models import Report
from .serializers import CenterReportSerializer, ReportSerializer


class DonorReportListView(ListAPIView):
    permissions = [
        permissions.IsAuthenticated,
        isPermittedDonor
    ]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class DonorReportRetrieveView(RetrieveAPIView):
    permissions = [
        permissions.IsAuthenticated,
        isPermittedDonor
    ]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class CenterReportUpdateView(UpdateAPIView):
    # lookup_field = "donor"
    queryset = Report.objects.all()
    permissions = [
        permissions.IsAuthenticated,
        centerIsPermitted,
    ]
    serializer_class = CenterReportSerializer


