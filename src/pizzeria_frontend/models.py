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
    client = models.CharField(max_length=100)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Orden {self.id} - {self.client} - {self.total} - {self.date}'

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    toppings = models.ManyToManyField(Topping, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pizza {self.size}'

    def calculate_pizza_price(self):
        price = 0
        price += self.size.price
        for topping in self.toppings.all():
            price += topping.price

    # def save(self, *args, **kwargs):
    #     if not Pizza.objects.filter(id=self.id):
    #         super(Pizza, self).save(*args, **kwargs)
    #     else:
    #         price = Decimal('0.00')
    #         if self.size:
    #             price = self.size.price

    #         for topping in self.toppings.all():
    #             if topping.price:
    #                 price = price + topping.price

    #         self.price = Decimal(str(price)).quantize(quant)
    #         super(Pizza, self).save(*args, **kwargs)
