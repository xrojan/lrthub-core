# Created by Joshua de Guzman on 07/07/2018
# @email code@jmdg.io
from rest_framework.response import Response
from ..models import Company
from . import serializers
from rest_framework import generics, status


class CompanyDetail(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer

    def list(self, request, *args, **kwargs):
        serializer = serializers.CompanySerializer(self.get_queryset(), many=True)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully retrieved", "result": data}
        return Response(response)
