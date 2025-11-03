from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import DustBin, BinReading, Alert
from .serializers import BinReadingSerializer, BinStatusSerializer

class DustBinViewSet(viewsets.ModelViewSet):
    queryset = DustBin.objects.all()
    serializer_class = BinStatusSerializer
    lookup_field = 'bin_id'

    @action(detail=True, methods=['post'])
    def update_reading(self, request, bin_id=None):
        try:
            bin_obj = self.get_object()
            
            # Create new reading
            reading_data = {
                'bin': bin_obj.id,
                'fill_percentage': request.data.get('fill_percentage'),
                'distance_cm': request.data.get('distance_cm'),
                'battery_level': request.data.get('battery_level'),
                'wifi_signal': request.data.get('wifi_signal')
            }
            
            serializer = BinReadingSerializer(data=reading_data)
            if serializer.is_valid():
                reading = serializer.save()
                
                # Check for alert condition
                alert_triggered = reading.fill_percentage >= bin_obj.threshold
                if alert_triggered:
                    Alert.objects.create(
                        bin=bin_obj,
                        fill_percentage=reading.fill_percentage
                    )
                
                return Response({
                    'status': 'success',
                    'message': 'Data received and logged successfully.',
                    'alert_triggered': alert_triggered,
                    'threshold': bin_obj.threshold,
                    'bin_status': 'Overflow Detected' if alert_triggered else 'Normal',
                    'next_action': 'Notify municipal collection team.' if alert_triggered else None
                })
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def status(self, request):
        bins = self.get_queryset()
        serializer = self.get_serializer(bins, many=True)
        return Response({'bins': serializer.data})
