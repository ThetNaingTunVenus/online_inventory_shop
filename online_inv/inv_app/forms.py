from django import forms
from .models import Product

class CreateProduct(forms.ModelForm):
    models = Product
    field = ['category_name','name', 'purchase_price','sale_price']