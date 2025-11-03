from rest_framework import serializers
from .models import DustBin, BinReading

class BinReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinReading
        fields = '__all__'

class BinStatusSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    last_updated = serializers.SerializerMethodField()
    fill_percentage = serializers.SerializerMethodField()

    class Meta:
        model = DustBin
        fields = ['bin_id', 'location_name', 'fill_percentage', 
                 'status', 'last_updated', 'latitude', 'longitude']