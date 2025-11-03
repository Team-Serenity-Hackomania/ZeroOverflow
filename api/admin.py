from django.contrib import admin
from .models import DustBin, BinReading, Alert

@admin.register(DustBin)
class DustBinAdmin(admin.ModelAdmin):
    list_display = ('bin_id', 'location_name', 'capacity_liters', 'threshold')
    search_fields = ('bin_id', 'location_name')
    list_filter = ('threshold',)

@admin.register(BinReading)
class BinReadingAdmin(admin.ModelAdmin):
    list_display = ('bin', 'fill_percentage', 'battery_level', 'timestamp')
    list_filter = ('bin', 'timestamp')
    date_hierarchy = 'timestamp'

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('bin', 'fill_percentage', 'created_at', 'resolved')
    list_filter = ('resolved', 'created_at')
    date_hierarchy = 'created_at'
