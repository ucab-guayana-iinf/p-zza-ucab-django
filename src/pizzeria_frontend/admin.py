from django.contrib import admin
from .models import Topping, Order, Pizza, Size

# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'size', 'price', 'order']

class PizzaInline(admin.TabularInline):
    model = Pizza
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    # readonly_fields = ['date']
    fieldsets = [
        (None, {'fields': ['client', 'price']}),
        # ('Fecha de publicación', {'fields': ['pub_date'], 'classes': ['collapseXDDDDDDDD']}),
    ]
    inlines = [PizzaInline]
    list_display = ['id', 'client', 'price', 'date']
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

admin.site.register(Topping)
admin.site.register(Size)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Order, OrderAdmin)