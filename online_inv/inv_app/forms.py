from django import forms
from .models import Product

class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category_name','name', 'purchase_price','sale_price']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'purchase_price': forms.TextInput(attrs={'class': 'form-control'}),
            'sale_price': forms.TextInput(attrs={'class': 'form-control'}),

        }