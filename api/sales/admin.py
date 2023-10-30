from django.contrib import admin
from .models import DailySales, SaleTransaction
from import_export.admin import ImportExportActionModelAdmin

class DailySalesDetail(admin.ModelAdmin):
    list_display = [
        "time",
        "sales",
        "grossProfit",
        "nProd"
    ]
admin.site.register(DailySales, DailySalesDetail)

class SaleTransactionAdmin(admin.ModelAdmin):
    class Meta:
        model = SaleTransaction
    list_display = [
        "id",
        "time",
        "customer_id",
        "product_id",
        "number_sales",
    ]
admin.site.register(SaleTransaction, SaleTransactionAdmin)

class DailySalesAdmin(ImportExportActionModelAdmin):
    pass