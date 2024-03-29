from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AppointmentViewSet,
    BloodCenterAppointments,
    DonorsAppointments,
    RequestBlood
)
# .


router = DefaultRouter()
router.register('', AppointmentViewSet)



urlpatterns = [
    # Blood Center Appointments
    path(
        'blood-center/<uuid:blood_center>/', 
        BloodCenterAppointments.as_view(), 
        name='blood_center_list_update_appointments'
    ),
    # Donor Appointments
    path(
        'donor/<uuid:donor_id>/', 
        DonorsAppointments.as_view(), 
        name='donor_list_appointments'
    ),
    path('requestblood/', RequestBlood.as_view())
]

urlpatterns += router.urls
