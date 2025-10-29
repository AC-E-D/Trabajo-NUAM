from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Producto, Venta, DetalleVenta

# -------------------------
# LOGIN Y LOGOUT
# -------------------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu_principal')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


# -------------------------
# MENÚ PRINCIPAL
# -------------------------
@login_required
def menu_principal(request):
    return render(request, 'menu_principal.html')


# -------------------------
# CRUD PRODUCTOS
# -------------------------
@login_required
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

@login_required
def producto_create(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
        return redirect('producto_list')
    return render(request, 'producto_form.html')

@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.save()
        return redirect('producto_list')
    return render(request, 'producto_form.html', {'producto': producto})

@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})


# -------------------------
# CRUD VENTAS
# -------------------------
@login_required
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'venta_list.html', {'ventas': ventas})

@login_required
def venta_create(request):
    if request.method == 'POST':
        fecha = request.POST['fecha']
        total = request.POST['total']
        Venta.objects.create(fecha=fecha, total=total)
        return redirect('venta_list')
    return render(request, 'venta_form.html')

@login_required
def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('venta_list')
    return render(request, 'venta_confirm_delete.html', {'venta': venta})


# -------------------------
# CRUD DETALLE DE VENTA
# -------------------------
@login_required
def detalleventa_list(request):
    detalles = DetalleVenta.objects.all()
    return render(request, 'detalleventa_list.html', {'detalles': detalles})

@login_required
def detalleventa_create(request):
    ventas = Venta.objects.all()
    productos = Producto.objects.all()

    if request.method == 'POST':
        venta_id = request.POST['venta_id']
        producto_id = request.POST['producto_id']
        cantidad = int(request.POST['cantidad'])
        subtotal = float(request.POST['subtotal'])

        DetalleVenta.objects.create(
            venta_id=venta_id,
            producto_id=producto_id,
            cantidad=cantidad,
            subtotal=subtotal
        )
        return redirect('detalleventa_list')

    return render(request, 'detalleventa_form.html', {'ventas': ventas, 'productos': productos})

@login_required
def detalleventa_delete(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == 'POST':
        detalle.delete()
        return redirect('detalleventa_list')
    return render(request, 'detalleventa_confirm_delete.html', {'detalle': detalle})
