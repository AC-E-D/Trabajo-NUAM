from django.urls import path
from . import views

urlpatterns = [
    # Login y Logout
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Menú principal
    path('menu/', views.menu_principal, name='menu_principal'),

    # CRUD Productos
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),
    path('productos/editar/<int:pk>/', views.producto_update, name='producto_update'),
    path('productos/eliminar/<int:pk>/', views.producto_delete, name='producto_delete'),

    # CRUD Ventas
    path('ventas/', views.venta_list, name='venta_list'),
    path('ventas/nueva/', views.venta_create, name='venta_create'),
    path('ventas/eliminar/<int:pk>/', views.venta_delete, name='venta_delete'),

    # CRUD DetalleVenta
    path('detalles/', views.detalleventa_list, name='detalleventa_list'),
    path('detalles/nuevo/', views.detalleventa_create, name='detalleventa_create'),
    path('detalles/eliminar/<int:pk>/', views.detalleventa_delete, name='detalleventa_delete'),
]
