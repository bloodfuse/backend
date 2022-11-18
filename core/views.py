from django.http import JsonResponse
from core.serializers import BloodCentersSerializer, DonorSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import AllowAny, IsAdmin

from core.models import User



@api_view()
def index(request):
    return JsonResponse({"message": "Welcome to bloodfuse API."})


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user = UserSerializer.details(user)

        return Response(user.data, status=status.HTTP_200_OK)

class DonorListView(ListAPIView):
    queryset = User.objects.filter(account_type="donor")
    permission_classes = [IsAuthenticated]
    serializer_class = DonorSerializer

class BloodCentersListView(ListAPIView):
    queryset = User.objects.filter(account_type="donation_center")
    permission_classes = [IsAuthenticated]
    serializer_class = BloodCentersSerializer

