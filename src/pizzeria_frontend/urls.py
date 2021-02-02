from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    path('order/', views.OrderCreateView.as_view(), name='order'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    # path('pizza/', views.pizza_order_view, name='pizza'),
]
