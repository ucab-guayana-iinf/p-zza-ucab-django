from django.urls import path

from . import views
app_name = 'pizzeria_frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.OrderCreateView.as_view(), name='order'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('orders-by-date/', views.OrdersByDateView.as_view(), name='orders-by-date'),
    path('orders-by-size/', views.OrdersBySizeView.as_view(), name='orders-by-size'),
    path('orders-by-topping/', views.OrdersByToppingView.as_view(), name='orders-by-topping'),
    path('orders-by-client/', views.OrdersByClientView.as_view(), name='orders-by-client'),
]
