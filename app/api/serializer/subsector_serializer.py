from rest_framework import serializers
from app import models
from app.api.serializer.indicator_serializer import IndicatorSerializer
class SubsectorSerializer(serializers.ModelSerializer):
    indicators = IndicatorSerializer(many=True)
    class Meta:
        model = models.Subsector
        fields = '__all__'
