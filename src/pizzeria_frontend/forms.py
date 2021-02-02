from django import forms
from .models import Pizza, Order

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'price', 'order', 'toppings']