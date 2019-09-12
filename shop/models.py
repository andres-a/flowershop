from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

class OrderHeader(models.Model):
    date = models.DateTimeField()
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)

class OrderLine(models.Model):
    order = models.ForeignKey(OrderHeader, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
