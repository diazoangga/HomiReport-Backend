import os
import pandas as pd
from tablib import Dataset
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import permissions, status, viewsets, generics

from .models import DailySales
from .resources import DailySalesResource
from .serializers import DailySalesSerializer

# Create your views here.
@api_view(['POST'])
def parse_daily_sales(request):
    if request.method == 'POST':
        # UploadFileForm(request.POST, request.FILES)
        # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # excel_data = pd.read_excel(filename, 'Sheet1', skiprows=11)
        # dbframe = excel_data
        # for dbframe in dbframe.itertuples():
        #     obj = DailySales.objects.create(time=dbframe[HEADER_NAME[0]], sales=dbframe[HEADER_NAME[1]],
        #                                     grossProfit=dbframe[HEADER_NAME[2]], nProd=dbframe[HEADER_NAME[7]])
        #     obj.save()
        # return Response(obj, status=status.HTTP_201_CREATED)

        # daily_sales_resource = DailySalesResource()
        # dataset = Dataset()
        # new_sales_data = request.FILES['myfile']
        # imported_data = dataset.load(new_sales_data.read(), format='xslx')
        # for data in imported_data:
        pass

    return render(request, '.form.html')

    
    # elif request.method =='GET':
    #     # sales_prop = DailySales.objects.all()
    #     # serializer = DailySalesResource(sales_prop)
    #     return Response('halo')

def income(request):
    return HttpResponse("this is page of incomes")

class DailySalesViewSets(viewsets.ViewSet):
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