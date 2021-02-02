from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Order, Pizza
from .forms import PizzaForm

# def index(request):
#     return HttpResponse("Hola")

def pizza_create_view(request):
    form = PizzaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PizzaForm() # para limpiar el form al finalizar

    context = {
        'form': form
    }
    return render(request, 'pizzeria_frontend/pizza_create.html', context)

class IndexView(generic.ListView):
    template_name = 'pizzeria_frontend/index.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        """Return orders."""
        return Order.objects.all

class DetailView(generic.DetailView):
    model = Order
    template_name = 'pizzeria_frontend/detail.html'