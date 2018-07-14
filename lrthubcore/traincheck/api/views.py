# Created by Joshua de Guzman on 15/07/2018
# @email code@jmdg.io

from rest_framework.response import Response
from ..models import TrainCheckHistory
from . import serializers
from rest_framework import generics, status


class TrainCheckList(generics.ListAPIView):
    queryset = TrainCheckHistory.objects.all()
    serializer_class = serializers.TrainCheckHistory

    def list(self, request, *args, **kwargs):
        serializer = serializers.TrainCheckHistorySerializer(self.get_queryset(), many=True)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully retrieved", "result": data}
        return Response(response)
