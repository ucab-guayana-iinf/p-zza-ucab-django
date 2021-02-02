from django.db import models

# Create your models here.
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
    price = models.DecimalField(decimal_places=2, max_digits=20)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Orden de {self.client} por {self.price} el {self.date}'

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    toppings = models.ManyToManyField(Topping)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pizza {self.size}'

