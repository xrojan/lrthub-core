# Created by Joshua de Guzman on 05/07/2018
# @email code@jmdg.io
from ..models import Feed, FeedType
from . import serializers
from . import pagination
from rest_framework import generics, status
from rest_framework.response import Response


class FeedList(generics.ListCreateAPIView):
    serializer_class = serializers.FeedSerializers
    pagination_class = pagination.CustomPagination

    def get_queryset(self):
        queryset = Feed.objects.all()
        is_on_main_page = self.request.GET.get('is_on_main_page', None)

        if is_on_main_page is not None and (is_on_main_page.lower() == 'true' or is_on_main_page.lower() == 'false'):
            is_on_main_page = is_on_main_page[0].upper() + is_on_main_page[1:].lower()
            return queryset.filter(type_id__is_on_main_page=is_on_main_page)
        else:
            return queryset

    def create(self, request, *args, **kwargs):
        super(FeedList, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully created", "result": request.data}
        return Response(response)


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = serializers.FeedSerializers

    def retrieve(self, request, *args, **kwargs):
        super(FeedDetail, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully retrieved", "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(FeedDetail, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully updated", "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(FeedDetail, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK, "message": "Successfully deleted"}
        return Response(response)
