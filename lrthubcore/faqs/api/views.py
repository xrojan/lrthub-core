# Created by Joshua de Guzman on 12/07/2018
# @email code@jmdg.io
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..models import Faq
from .serializers import FaqSerializer
from rest_framework import generics, status


class FaqList(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Faq.objects.all()
    serializers = FaqSerializer

    def list(self, request, *args, **kwargs):
        serializer = FaqSerializer(self.get_queryset(), many=True)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully retrieved", "result": data}
        return Response(response)
