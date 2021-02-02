from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.forms import formset_factory
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from .models import Order, Pizza, Topping
from .forms import PizzaForm, MultiplePizzaForm, OrderForm, PizzaFormset

def index(request):
    # return HttpResponse("Hola")
    return redirect('order/')

# Vista para hacer un pedido usando vista generica
class OrderCreateView(CreateView):
    model = Order
    fields = ['client']

    # we need to overwrite get_context_data to make sure that our formset is rendered
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["pizzas"] = PizzaFormset(self.request.POST)
        else:
            data["pizzas"] = PizzaFormset()
        return data

    # we need to overwrite get_context_data to make sure that our formset is rendered
    def form_valid(self, form):
        context = self.get_context_data()
        pizzasFormset = context["pizzas"]
        self.object = form.save() # saves parent object (order)
        if pizzasFormset.is_valid():
            pizzasFormset.instance = self.object # sets the parent object instance (associates pizza to order)
            pizzasFormset.save()
            # super().form_valid(form) esto envia a get_success_url
            return HttpResponseRedirect(reverse('order-detail', args=(self.object.id,)))

    # si no se define esto el default se redirige al object.get_absolute_url()
    def get_success_url(self):
        return reverse(reverse('order-detail', args=(self.object.id,)))

# def pizza_order_view(request):
#     clicked = False
#     topping_list = Topping.objects.all()
#     pizza_form = PizzaForm(request.POST or None)
#     order_form = OrderForm(request.POST or None)

#     if pizza_form.is_valid() and order_form.is_valid():
#         clicked = True
#         # form.save()
#         print(request.POST)
#         pizza_form = PizzaForm() # para limpiar el form al finalizar
#         order_form = OrderForm()
#     elif order_form.is_valid():
#         print(request.POST)

#     context = {
#         'pizza_form': pizza_form,
#         'order_form': order_form,
#         'topping_list': topping_list,
#         'clicked': clicked
#     }
#     return render(request, 'pizzeria_frontend/pizza_create.html', context)

class IndexView(generic.ListView):
    template_name = 'pizzeria_frontend/index.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        """Return orders."""
        return Order.objects.all

class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'pizzeria_frontend/detail.html'
    