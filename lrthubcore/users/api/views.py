# Created by Joshua de Guzman on 09/07/2018
# @email code@jmdg.io
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


class UserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                response = {"status_code": status.HTTP_201_CREATED,
                            "message": "Successfully created",
                            "result": request.data}
                return Response(response)
        response = {"status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "Failed to create user",
                    "result": serializer.errors}
        return Response(response)
