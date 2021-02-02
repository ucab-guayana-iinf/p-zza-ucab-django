from django.contrib import admin
from .models import Topping, Order, Pizza, Size

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'size', 'order', 'pizza_price']
    list_filter = ['size']

class PizzaInline(admin.TabularInline):
    model = Pizza
    extra = 1
    exclude = ['price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'order_price', 'date']
    list_filter = ['date', 'client']
    exclude = ['total']
    inlines = [PizzaInline]
    # search_fields = ['question_text']

admin.site.register(Topping, ItemAdmin)
admin.site.register(Size, ItemAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Order, OrderAdmin)