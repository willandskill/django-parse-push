from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import DeviceSerializer


class DeviceTokenSetter(APIView):
    """
    Set a push token related to device for signed in User
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.DATA)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED)
