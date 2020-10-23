from django.shortcuts import render, HttpResponse,redirect
from .forms import CreateProduct
from .models import Product


# Create your views here.

def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def index(request):
    fm = CreateProduct(request.POST or None)
    products = Product.objects.all()
    context = {"form": fm, "products": products}
    return render(request, 'index.html', context)


def product_list(request):

    products = Product.objects.all()


    context = {"products": products}
    return render(request, 'product_list.html', context)






def create_product(request):
    fm = CreateProduct()
    if request.method == 'POST':
        fm = CreateProduct(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('product_list')
        else:
            return HttpResponse("invlaid form")


    return render(request, 'create_product.html',{"form":fm})


def delete_product(request,id):
    if request.method=='POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return redirect('product_list')


def edit_product(request,id):
    if request.method=='POST':
        pi = Product.objects.get(pk=id)
        fm = CreateProduct(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('product_list')
    else:
        pi = Product.objects.get(pk=id)
        fm = CreateProduct(instance=pi)
    return render(request, 'edit_product.html', {"form":fm})