from rest_framework import serializers
from .models import DustBin, BinReading

class BinReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinReading
        fields = '__all__'

class BinStatusSerializer(serializers.ModelSerializer):
    fill_percentage = serializers.SerializerMethodField()
    last_updated = serializers.SerializerMethodField()

    class Meta:
        model = DustBin
        fields = ['bin_id', 'location_name', 'latitude', 'longitude', 
                 'capacity_liters', 'threshold', 'fill_percentage', 'last_updated']

    def get_fill_percentage(self, obj):
        latest_reading = BinReading.objects.filter(bin=obj).order_by('-timestamp').first()
        return latest_reading.fill_percentage if latest_reading else 0

    def get_last_updated(self, obj):
        latest_reading = BinReading.objects.filter(bin=obj).order_by('-timestamp').first()
        return latest_reading.timestamp if latest_reading else None