from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index')
    path('', views.IndexView.as_view(), name='index'),
    path('pizza/', views.pizza_order_view, name='pizza'),
    path('test/', views.testView.as_view(), name='test'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
