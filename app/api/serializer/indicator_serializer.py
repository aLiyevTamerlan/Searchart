from rest_framework import serializers
from app import models

class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Indicator
        fields = '__all__'