from import_export import resources
from .models import DailySales

class DailySalesResource(resources.ModelResource):
    class Meta:
        model = DailySales
        fields = ['id',
                  'time',
                  'sales',
                  'grossProfit',
                  'nProd']

    def after_import_row(self, row, row_result, row_number=None, **kwargs):
        return super().after_import_row(row, row_result, row_number, **kwargs)
    
    def before_import_row(self, row, row_number=None, **kwargs):
        obj = DailySales.objects.all()
        # field_obj = DailySales._meta.get_field('time')
        for f in obj:
            field_value = getattr(f, 'time')
            # print(row['time'], field_value.type)
            if str(row['time']) == str(field_value):
                f.delete()
                # print('DELETED THE ROW')
        return super().before_import_row(row, row_number, **kwargs)