from django.urls import path, include
from rest_framework import routers

from .views import (
    # UserViewSet, 
    index, 
    DonorListView,
    BloodCentersListView,
    UserView,
)



router = routers.DefaultRouter()
router.register("user", UserViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('user/', UserView.as_view, name="user_view"),
    path('users/donors/', DonorListView.as_view(), name='donor_list'),
    path('users/blood-centers/', BloodCentersListView.as_view(), name='blood_centers_list'),
]

urlpatterns += router.urls
