# Created by Joshua de Guzman on 09/07/2018
# @email code@jmdg.io
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .. import models
from . import serializers


class UserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
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


class UserProfileGenderList(generics.ListAPIView):
    queryset = models.Gender.objects.all()
    serializer_class = serializers.GenderSerializer


class UserProfileNationalityList(generics.ListAPIView):
    queryset = models.Nationality.objects.all()
    serializer_class = serializers.NationalitySerializer


class UserProfileMaritalStatusList(generics.ListAPIView):
    queryset = models.MaritalStatus.objects.all()
    serializer_class = serializers.MaritalStatusSerializer


class UserProfileEmploymentTypeList(generics.ListAPIView):
    queryset = models.EmploymentType.objects.all()
    serializer_class = serializers.EmploymentTypeSerializer


class UserProfileDisabilityList(generics.ListAPIView):
    queryset = models.Disability.objects.all()
    serializer_class = serializers.DisabilitiesSerializer


class UserProfileList(generics.ListCreateAPIView):
    serializer_class = serializers.UserProfileSerializer

    def get_queryset(self):
        queryset = models.UserProfile.objects.all()
        user_id = int(self.request.GET.get('user_id', None))
        return queryset.filter(user_id=user_id)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        request_user_id = int(request.POST.get('user_id', ''))

        if user.id == request_user_id:
            super(UserProfileList, self).create(request, args, kwargs)
            response = {"status_code": status.HTTP_201_CREATED,
                        "message": "Successfully created",
                        "result": request.data}
            return Response(response)

        response = {"status_code": status.HTTP_403_FORBIDDEN,
                    "message": "You are not allowed to continue with the request",
                    "result": request.data}
        return Response(response)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        request_user_id = self.kwargs['pk']

        if user.id == request_user_id:
            super(UserProfileDetail, self).retrieve(request, args, kwargs)
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            response = {"status_code": status.HTTP_200_OK,
                        "message": "Successfully retrieved",
                        "result": data}
            return Response(response)

        response = {"status_code": status.HTTP_403_FORBIDDEN,
                    "message": "You are not allowed to continue with the request",
                    "result": request.data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        request_user_id = self.kwargs['pk']

        if user.id == request_user_id:
            super(UserProfileDetail, self).patch(request, args, kwargs)
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            data = serializer.data
            response = {"status_code": status.HTTP_200_OK,
                        "message": "Successfully updated",
                        "result": data}
            return Response(response)

        response = {"status_code": status.HTTP_403_FORBIDDEN,
                    "message": "You are not allowed to continue with the request",
                    "result": request.data}
        return Response(response)
