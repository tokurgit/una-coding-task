from glucose_checker.api.models import GlucoseReading

from rest_framework import serializers, filters


class GlucoseReadingSerializer(serializers.ModelSerializer):

    # TODO Add date field and validate it
    # with datetime.strptime("dd-mm-yyyy hh:mm", "%d-%m-%Y %H:%M")

    class Meta:
        model = GlucoseReading
        fields = "__all__"
