__author__ = 'MatthewHan'
from django import forms
from decimal import Decimal
class AddProductForm(forms.Form):
    name = forms.CharField(min_length=8,label='Name')
    MANUFACTURERS = [
        ('Kenneth Cole', 'Kenneth Cole'),
        ('Gap', 'Gap'),
        ('Samsung', 'Samsung'),
    ]
    manufacturer = forms.ChoiceField(choices=MANUFACTURERS)
    price = forms.DecimalField(max_digits=10,decimal_places=2,min_value = Decimal("0.01"))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),max_length=50)
