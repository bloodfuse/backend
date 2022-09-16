from django.urls import path

from .views import (
    DonorReportListView,
    DonorReportRetrieveView,
    CenterReportUpdateView,
)


urlpatterns = [
    path("donor/", DonorReportListView.as_view(), name='donor_reports'),
    path("donor/<uuid:pk>/", DonorReportRetrieveView.as_view(), name='get_donor_report'),
    path("center/<uuid:pk>/", CenterReportUpdateView.as_view(), name='center_update_report'),
]