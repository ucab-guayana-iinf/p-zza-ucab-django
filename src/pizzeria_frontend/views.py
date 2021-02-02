from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.forms import formset_factory
from django.views.generic.edit import CreateView, UpdateView
from django.forms.models import inlineformset_factory

from .models import Order, Pizza, Topping
from .forms import PizzaForm, MultiplePizzaForm, OrderForm

# def index(request):
#     return HttpResponse("Hola")

PizzaFormset = inlineformset_factory(Order, Pizza, fields=('size', 'toppings'), extra=1, can_delete=False)

class testView(CreateView):
    model = Order
    fields = ['client']

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["pizzas"] = PizzaFormset(self.request.POST)
        else:
            data["pizzas"] = PizzaFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pizzasFormset = context["pizzas"]
        self.object = form.save() # saves parent object (order)
        if pizzasFormset.is_valid():
            pizzasFormset.instance = self.object # sets the parent object instance (associates pizza to order)
            pizzasFormset.save()
        return super().form_valid(form)

    # si no se define esto el default se redirige al object.get_absolute_url()
    def get_success_url(self):
        return reverse('pizza')

def pizza_order_view(request):
    clicked = False
    topping_list = Topping.objects.all()
    pizza_form = PizzaForm(request.POST or None)
    order_form = OrderForm(request.POST or None)

    if pizza_form.is_valid() and order_form.is_valid():
        clicked = True
        # form.save()
        print(request.POST)
        pizza_form = PizzaForm() # para limpiar el form al finalizar
        order_form = OrderForm()
    elif order_form.is_valid():
        print(request.POST)

    context = {
        'pizza_form': pizza_form,
        'order_form': order_form,
        'topping_list': topping_list,
        'clicked': clicked
    }
    return render(request, 'pizzeria_frontend/pizza_create.html', context)

# def pizza_order_view(request):
# # Control de cuantas veces se presentara el form de cada pizza
# number_of_pizzas = 1
# multi_pizza = MultiplePizzaForm()
# if multi_pizza.is_valid():
#     number_of_pizzas = multi_pizza.cleaned_data['number']

# # Formularios de pizzas individuales
# PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
# formset = PizzaFormSet()

# # form = PizzaForm(request.POST or None)
# topping_list = Topping.objects.all()
# if request.method == 'POST':
#     if formset.is_valid():
#         print('formset data:')
#         for form in formset:
#             print(form.cleaned_data)

# # if request.method == 'POST':
# #     print('POST AAA', request.POST)
# #     if form.is_valid():
# #         # form.save()
# #         form = PizzaForm() # para limpiar el form al finalizar

# context = {
#     # 'form': form,
#     'multi_pizza_form': multi_pizza,
#     'formset': formset,
#     'topping_list': topping_list
# }
# return render(request, 'pizzeria_frontend/pizza_create.html', context)

class IndexView(generic.ListView):
    template_name = 'pizzeria_frontend/index.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        """Return orders."""
        return Order.objects.all

class DetailView(generic.DetailView):
    model = Order
    template_name = 'pizzeria_frontend/detail.html'
    