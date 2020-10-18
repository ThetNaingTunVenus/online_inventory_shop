from django.shortcuts import render,HttpResponse
from .forms import CreateProduct
from .models import Product

# Create your views here.
def index(request):
    fm = CreateProduct(request.POST or None)
    context = {"form":fm}
    return render(request, 'index.html', context)