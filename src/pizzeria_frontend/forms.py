from django import forms
from django.forms.models import inlineformset_factory

from .models import Pizza, Order, Size

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client']

class PizzaForm(forms.ModelForm):
    class Meta:
        model   = Pizza
        fields = ['size', 'toppings']

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=1) #max_value=6