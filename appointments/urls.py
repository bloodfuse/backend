from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AppointmentViewSet,
    BloodCenterAppointments,
    DonorsAppointments,
    DonorAppointments,
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
    path('donor/<uuid:donor_id>/', DonorAppointments.as_view()),
    path('donors/', DonorsAppointments.as_view()),
    path('requestblood/', RequestBlood.as_view())
]

urlpatterns += router.urls
