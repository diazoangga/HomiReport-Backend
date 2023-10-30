from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions, status, viewsets, generics

from .models import DailySales

class ExpensesViewSets(viewsets.ViewSet):
    def list(self, request):
        sales = DailySales.objects.all()
        sales_serializer = DailySalesSerializer(sales, many=True)
        return Response(sales_serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        sales = DailySales.objects.all()
        sale = get_object_or_404(sales, pk=pk)
        sales_serializer = DailySalesSerializer(sale)
        return Response(sales_serializer.data)
    
    def create(self, request):
        sales_data = request.data
        new_sales = DailySales.objects.create(time=sales_data['time'],
                                              sales=sales_data['sales'],
                                              grossProfit=sales_data['grossProfit'],
                                              nProd=sales_data['nProd'])
        new_sales.save()

        serializer = DailySalesSerializer(new_sales)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk=None):
        sales = DailySales.objects.all()
        sale = get_object_or_404(sales, pk=pk)
        sale.delete()

        return Response({"Status": "Successfully delete id: {id}"}, status=status.HTTP_204_NO_CONTENT)

    
    @action(detail=False, methods=['delete', 'get'])
    def destroy_all(self, request):
        sales = DailySales.objects.all()
        sales.delete()

        return Response({"Status": "Sucessfully delete all of the data"}, status=status.HTTP_204_NO_CONTENT)