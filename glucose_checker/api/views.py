from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from django_filters import rest_framework as filters

from glucose_checker.api.models import GlucoseReading
from glucose_checker.api.serializers import GlucoseReadingSerializer
from glucose_checker.api.utils import convert_date_str_to_datetime

class GlucoseReadingViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """API endpoints related to the GlucoseReading."""
    queryset = GlucoseReading.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    serializer_class = GlucoseReadingSerializer

    def list(self, request):
        start = convert_date_str_to_datetime(request.query_params.get("start"))
        stop = convert_date_str_to_datetime(request.query_params.get("stop"))
        user_id = request.query_params.get("user_id")
        readings = self.queryset

        filter_params = {}
        if user_id:
            filter_params["user_id"] = user_id
        if start and stop:
            filter_params["reading_time__gte"] = [start, stop]
        elif start:
            filter_params["reading_time__gte"] = start
        elif stop:
            filter_params["reading_time__lte"] = stop

        readings = GlucoseReading.objects.filter(**filter_params)
        serializer = GlucoseReadingSerializer(readings, many=True)
        return Response(serializer.data)
