# Created by Joshua de Guzman on 07/07/2018
# @email code@jmdg.io

from rest_framework.response import Response
from ..models import Rating
from . import serializers
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated


class RatingList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer


class RatingCreate(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer

    def create(self, request, *args, **kwargs):
        super(RatingCreate, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully created", "result": request.data}
        return Response(response)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Rating.objects.all()
    serializer_class = serializers.RatingSerializer

    def retrieve(self, request, *args, **kwargs):
        super(RatingDetail, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully retrieved", "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(RatingDetail, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully updated", "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(RatingDetail, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully deleted"}
        return Response(response)
