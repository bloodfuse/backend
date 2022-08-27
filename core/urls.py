from django.urls import path, include
from rest_framework import routers

from .views import (
    UserViewSet, 
    index, 
    DonorListView
)



router = routers.DefaultRouter()
router.register("user", UserViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('users/donors/', DonorListView.as_view(), name='donor_list'),
]

urlpatterns += router.urls
