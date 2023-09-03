from rest_framework import serializers
from .models import ImportSalesFile


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportSalesFile        
        fields = ['filename', 'added_at', 'status', 'processing_start_time']
        
