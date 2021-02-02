from django.contrib import admin
from .models import Topping, Order, Pizza, Size

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']

class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id', 'size', 'price', 'order']

class PizzaInline(admin.TabularInline):
    model = Pizza
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    # readonly_fields = ['date']
    # fieldsets = [
    #     (None, {'fields': ['client', 'price']}),
        # ('Fecha de publicación', {'fields': ['pub_date'], 'classes': ['collapseXDDDDDDDD']}),
    # ]
    inlines = [PizzaInline]
    list_display = ['id', 'client', 'total', 'date']
    # list_filter = ['pub_date']
    # search_fields = ['question_text']

admin.site.register(Topping, ItemAdmin)
admin.site.register(Size, ItemAdmin)
admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Order, OrderAdmin)