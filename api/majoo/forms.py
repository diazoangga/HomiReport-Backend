from django import forms
from .models import ImportSalesFile

class ImportFileModelForm(forms.ModelForm):
    class Meta:
        model = ImportSalesFile
        fields = '__all__'