from django.contrib import admin
from django.urls import path, include
from bloodfuse.view import redirect_to_index
from rest_framework import permissions

# drf-yasg imports
from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# rest_framework_simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from dj_rest_auth.views import PasswordResetConfirmView
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

from .view import CustomEmailVerification

from django.conf import settings
from django.conf.urls.static import static


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
    # Site / Admin
    path('', redirect_to_index, name="redirect_to_index"),
    path('_/', admin.site.urls),

    # dj-auth endpoints
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/register/', include('dj_rest_auth.registration.urls')),
    path(
        'api/register/account-confirm-email/<str:key>',
        # ConfirmEmailView.as_view(),
        CustomEmailVerification.as_view(),
        name='account_email'
    ),
    path(
        'api/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    path(
        'api/auth/password/reset/confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),

    # Swagger Api endpoints
    re_path(r'^api/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^api/swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^api/redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),

    # rest_framework_simplejwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view()),

    # other vApi
    path('api/', include('core.urls')),
    path('api/appointments/', include('appointments.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/endpoints/', include('endpoint.urls')),
]

'''
This above re_path exposes 4 endpoints:

    A JSON view of your API specification at /api/swagger.json
    A YAML view of your API specification at /api/swagger.yaml
    A swagger-ui view of your API specification at /api/swagger/
    A ReDoc view of your API specification at /api/redoc/

'''


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
