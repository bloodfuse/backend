from django.urls import path, include
from rest_framework import routers

from .views import (UserViewSet, index)



router = routers.DefaultRouter()
router.register("user", UserViewSet)

urlpatterns = [
    path('', index, name="index"),
]

urlpatterns += router.urls
