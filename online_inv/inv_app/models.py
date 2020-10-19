from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    purchase_price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    

