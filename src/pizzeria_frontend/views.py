from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Order, Pizza

# def index(request):
#     return HttpResponse("Hola")

class IndexView(generic.ListView):
    template_name = 'pizzeria_frontend/index.html'
    context_object_name = 'orders_list'

    def get_queryset(self):
        """Return orders."""
        return Order.objects.all

class DetailView(generic.DetailView):
    model = Order
    template_name = 'pizzeria_frontend/detail.html'