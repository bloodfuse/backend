from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from .utils import (
    userInfo
)

from .serializers import (
    AnonymousVisitorSerializer as AVS,
    AllDonorSerializer as ADS
)

T = True
F = False


class AnonymousVisitorsAnalysis(APIView):
    """Creates Anonymous Visitors"""

    def post(self, requests):
        data = requests.data
        res = AVS.create(data)

        if res.data['status'] == 201:
            return Response(None, status=status.HTTP_201_CREATED)
        else:
            return Response(res.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AnonymousVisitorsAnalysisGet(APIView):
    """Read Anonymous Visitors"""

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, requests):
        user = requests.user

        # check = userInfo(user)
        check = F

        if check:
            res = AVS.read(user)

            if res.data['status'] == 200:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(res.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class AllDonors(APIView):
    """Read Anonymous Visitors"""

    permission_classes = [permissions.IsAuthenticated]

    def get(self, requests):
        user = requests.user

        isAdmin = userInfo(user)
        if isAdmin.role < 2000:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        elif isAdmin.role > 2000 and isAdmin.role < 9000:
            return Response(status=status.HTTP_403_FORBIDDEN)
        elif isAdmin.role > 9000:
            res = ADS.read()

            if res.data['status'] == 200:
                return Response(res.data['results'], status=status.HTTP_200_OK)
            else:
                return Response(res.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
