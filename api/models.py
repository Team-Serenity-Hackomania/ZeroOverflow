from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class DustBin(models.Model):
    bin_id = models.CharField(max_length=20, unique=True)
    location_name = models.CharField(max_length=100)
    capacity_liters = models.FloatField(default=50.0)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    threshold = models.IntegerField(
        default=80,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    
    def __str__(self):
        return f"{self.bin_id} - {self.location_name}"

class BinReading(models.Model):
    bin = models.ForeignKey(DustBin, on_delete=models.CASCADE, related_name='readings')
    fill_percentage = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    distance_cm = models.FloatField(null=True, blank=True)
    battery_level = models.IntegerField(null=True, blank=True)
    wifi_signal = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

class Alert(models.Model):
    bin = models.ForeignKey(DustBin, on_delete=models.CASCADE, related_name='alerts')
    fill_percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
