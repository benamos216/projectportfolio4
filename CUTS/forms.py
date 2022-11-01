from django import forms
from .models import Supplier, Range, Roll, Cut


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier']


class RangeForm(forms.ModelForm):
    class Meta:
        model = Range
        fields = ['supplier', 'ranges']


class RollForm(forms.ModelForm):
    class Meta:
        model = Roll
        fields = ['ranges', 'colour', 'roll_width', 'rollsizes', 'location']
