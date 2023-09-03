from django.contrib import admin
from .models import DailySales
from import_export.admin import ImportExportActionModelAdmin

class DailySalesDetail(admin.ModelAdmin):
    list_display = [
        "time",
        "sales",
        "grossProfit",
        "nProd"
    ]
admin.site.register(DailySales, DailySalesDetail)

class DailySalesAdmin(ImportExportActionModelAdmin):
    pass