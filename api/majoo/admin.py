from django.contrib import admin
from .models import ImportSalesFile

# Register your models here.
class SalesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "added_at",
        "processing_start_time",
        "status",
    ]

admin.site.register(ImportSalesFile, SalesAdmin)