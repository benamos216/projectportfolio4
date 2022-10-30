from django import forms
from .models import Supplier, Range, Cut


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier']


class RangeForm(forms.ModelForm):
    class Meta:
        model = Range
        fields = ['supplier', 'ranges']
