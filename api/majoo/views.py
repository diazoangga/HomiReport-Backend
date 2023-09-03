import os
import pandas as pd
from tablib import Dataset
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import permissions, status, viewsets
from rest_framework import viewsets
import pandas as pd

from .models import ImportSalesFile
from .serializers import SalesSerializer
from .forms import ImportFileModelForm

from ..sales.views import parse_daily_sales
from ..sales.views import DailySalesViewSets
from ..sales.resources import DailySalesResource
from ..sales.serializers import DailySalesSerializer

from datetime import datetime
 

HEADER_NAME = ['Waktu', 'Penjualan (Rp.)', 'Laba Kotor (Rp.)',
               'Jumlah Transaksi', ' Order / Transaksi (Rp.) ',
               'Refund (Rp.)', 'Komisi (Rp.)', 'Jumlah Produk',
               'produk / Transaksi']

# def upload_file_view(request):
#     form = ImportFileModelForm(request.POST or None, request.FILES or None)
#     print(form.is_valid())
#     if form.is_valid():
#         form.save()
#         form = ImportFileModelForm()
#         try:
#             parse_daily_sales(form.objects.get(status=1))
#             form.objects.put(status=2)
#         except RuntimeError:
#             form.objects.put(status=3)
#     return render(request, 'majoo/upload.html', {'form': form})
#     # return HttpResponse("HUFT")

# class FileViewSet(viewsets.ModelViewSet):
#     queryset = ImportSalesFile.objects.all()
#     serializer_class = SalesSerializer
    
class FileViewSet(viewsets.ViewSet):
    serializer_class = SalesSerializer
    def list(self, request):
        files = ImportSalesFile.objects.all()
        serializer = self.serializer_class(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        filename = request.data['filename']

        import_file = ImportSalesFile.objects.create(
            filename=filename,
            status=ImportSalesFile.Statuses.REQUEST_IMPORTING,
            processing_start_time=datetime.now()
        )

        df = pd.read_excel(filename, sheet_name='Sheet1', skiprows=11, usecols="A:C,H")

        rename_columns = {"Waktu": "time",
                        "Penjualan (Rp.)": "sales",
                        "Laba Kotor (Rp.)": "grossProfit",
                        "Jumlah Produk": "nProd"}
        
        df.rename(columns=rename_columns, inplace=True)
        resource = DailySalesResource()

        dataset = Dataset().load(df)

        # print(dataset.__dict__)
        # print(resource.__dict__)

        result = resource.import_data(dataset, dry_run=True,
                                    raise_errors=True, exclude='id')
        
        # print(result.__dict__)

        
        
        if not result.has_errors():
            result = resource.import_data(dataset, dry_run=False)
            # print(dataset)
            # sales_serializer = DailySalesSerializer(result)
            # if sales_serializer.is_valid():
            #     sales_serializer.save()

            import_file.status = ImportSalesFile.Statuses.DONE
            import_file.save()
            return Response({"Status": "DATA IMPORTED SUCCESSFULLY"}, status=status.HTTP_201_CREATED)
        else:
            import_file.status = ImportSalesFile.Statuses.ERROR        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, pk=None):
        files = ImportSalesFile.objects.all()
        file = get_object_or_404(files, pk=pk)
        serializer = self.serializer_class(file)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def destroy(self, request, pk=None):
        try:
            files = ImportSalesFile.objects.get(pk=pk)
        except ImportSalesFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        files.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def sales_file_list(request):
    sales_prop = ImportSalesFile.objects.all()
    serializer = SalesSerializer(sales_prop, many=True)
    return Response(serializer.data)
    

class ImportSalesData(APIView):
    def get(self, request, format=None):
        sales_prop = ImportSalesFile.objects.all()
        serializer = SalesSerializer(sales_prop, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def post(self, request):
        serializer = SalesSerializer
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def sales_detail(request, id):
    try:
        sales_prop = ImportSalesFile.objects.get(pk=id)
    except ImportSalesFile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = SalesSerializer(sales_prop)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        serializer = SalesSerializer(sales_prop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        sales_prop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

