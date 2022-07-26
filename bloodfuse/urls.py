from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='BloodFuse API Endpoint')

urlpatterns = [
    path('docs/', schema_view),
    path('_/', admin.site.urls),
]
