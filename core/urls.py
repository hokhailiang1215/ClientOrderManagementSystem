from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('clients/add/', views.ClientCreateView.as_view(), name='client-add'),
    path('clients/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client-edit'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client-delete'),
    
    path('clients/export/', views.export_clients_csv, name='client-export'),
    

    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/add/', views.OrderCreateView.as_view(), name='order-add'),
    path('orders/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order-edit'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
    path('orders/export/', views.export_orders_csv, name='order-export'),
]
