from rest_framework import serializers
from app import models
from app.api.serializer.subsector_serializer import SubsectorSerializer
class SectorAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sector
        fields = '__all__'


class SectorSerializer(serializers.ModelSerializer):
    sub_sectors = SubsectorSerializer(many=True)
    class Meta:
        model = models.Sector
        fields = '__all__'