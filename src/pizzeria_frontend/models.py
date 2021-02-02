from django.db import models
import decimal
from decimal import Decimal

quant = Decimal('0.01')

class Size(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.name} ({self.price})'

class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.name} ({self.price})'

class Order(models.Model):
    client = models.CharField('Cliente', max_length=100)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    date = models.DateField('Fecha', auto_now_add=True)

    @property
    def order_price(self):
        price = 0
        for pizza in self.pizza_set.all():
            price += pizza.pizza_price
        return price

    def __str__(self):
        return f'Orden {self.id} - {self.client} - {self.total} - {self.date}'

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name="Tamaño")
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    toppings = models.ManyToManyField(Topping, blank=True, verbose_name="Ingredientes")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Orden")

    @property
    def pizza_price(self):
        price = 0
        price += self.size.price
        for topping in self.toppings.all():
            price += topping.price
        return price

    def __str__(self):
        return f'Pizza {self.size}'
