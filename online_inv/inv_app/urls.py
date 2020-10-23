from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('cart/', views.cart, name= 'cart'),
    path('product_list/', views.product_list, name='product_list'),
    path('create_product/', views.create_product, name='create_product'),
    path('delete_product/<int:id>/', views.delete_product, name= "delete_product"),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),


]
