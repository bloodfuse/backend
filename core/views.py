from django.http import JsonResponse
from core.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import AllowAny, IsAdmin

from core.models import User



@api_view()
def index(request):
    return JsonResponse({"message": "Welcome to bloodfuse API"})


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer