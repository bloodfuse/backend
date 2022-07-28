from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

# from .view import update_from_github

schema_view = get_swagger_view(title='BloodFuse API Endpoint')

urlpatterns = [
    path('docs/', schema_view),
    path('_/', admin.site.urls),
    # path("update_from_github", update_from_github, name="update_from_github"),
]
