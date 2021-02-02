from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.forms import formset_factory
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Count
from django.db.models.functions import TruncDay

from .models import Order, Pizza, Topping, Size
from .forms import PizzaForm, MultiplePizzaForm, OrderForm, PizzaFormset

# Vista principal de la aplicacion
def index(request):
    context = {}
    return render(request, 'pizzeria_frontend/index.html', context)

# Vista para hacer un pedido usando vista generica
class OrderCreateView(CreateView):
    model = Order
    fields = ['client']

    # sobreescribir get_context_data para poder pasar el inlineformset al template
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["pizzas"] = PizzaFormset(self.request.POST)
        else:
            data["pizzas"] = PizzaFormset()
        return data

    # sobreescribir form_valid para manejar el input del formulario valido
    def form_valid(self, form):
        context = self.get_context_data()
        pizzasFormset = context["pizzas"]
        self.object = form.save() # guarda el objeto padre (orden)
        if pizzasFormset.is_valid():
            pizzasFormset.instance = self.object # asocia cada pizza a la orden
            pizzasFormset.save()
            # super().form_valid(form) esto envia a get_success_url
            return HttpResponseRedirect(reverse('pizzeria_frontend:order-detail', args=(self.object.id,)))

    # si no se define esta funcion el default se redirige al object.get_absolute_url()
    def get_success_url(self):
        return reverse(reverse('order-detail', args=(self.object.id,)))

# Vista para mostrar el detalle de una orden
class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'pizzeria_frontend/detail.html'

# Vista para mostrar el listado de ordenes
class OrdersView(generic.ListView):
    template_name = 'pizzeria_frontend/orders.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        """Retorna todas las ordenes."""
        return Order.objects.order_by('-id')

# Vista para mostrar el recuento de ventas por fecha
class OrdersByDateView(generic.ListView):
    template_name = 'pizzeria_frontend/orders_by_date.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        """Retorna todas las ordenes agrupadas por dia."""
        return Order.objects.annotate(day=TruncDay('date')).values('day').annotate(count=Count('id')) 

# Vista para mostrar el recuento de ventas por tamaño
class OrdersBySizeView(generic.ListView):
    template_name = 'pizzeria_frontend/orders_by_size.html'
    context_object_name = 'sizes_list'

    def get_queryset(self):
        """Retorna todos los tamaños con sus relaciones de pizzas."""
        return Size.objects.all()

# Vista para mostrar el recuento de ventas por topping
class OrdersByToppingView(generic.ListView):
    template_name = 'pizzeria_frontend/orders_by_topping.html'
    context_object_name = 'toppings_list'

    def get_queryset(self):
        """Retorna todos los toppings con sus relaciones de pizzas."""
        return Topping.objects.all()

# Vista para mostrar el recuento de ventas por cliente
class OrdersByClientView(generic.ListView):
    template_name = 'pizzeria_frontend/orders_by_client.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        """Retorna todas las ordenes agrupadas por cliente."""
        return Order.objects.values('client').annotate(count=Count('id')).order_by('-count')
