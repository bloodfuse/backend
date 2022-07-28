from django.contrib import admin
from django.urls import path, include

# drf-yasg imports
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from .view import update_from_github

schema_view = get_schema_view(
    openapi.Info(
        title="BloodFuse API Endpoint",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    
    path('_/', admin.site.urls),
    # path("update_from_github", update_from_github, name="update_from_github"),
]

'''
This above re_path exposes 4 endpoints:

    A JSON view of your API specification at /swagger.json
    A YAML view of your API specification at /swagger.yaml
    A swagger-ui view of your API specification at /swagger/
    A ReDoc view of your API specification at /redoc/

'''