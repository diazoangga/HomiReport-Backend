from rest_framework import serializers
from .models import DailySales


class DailySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySales        
        fields = ['time', 
                  'sales', 
                  'grossProfit', 
                  'nProd']
        