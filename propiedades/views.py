from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Inmueble

@login_required
def home(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'home.html', {'inmuebles': inmuebles})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil_usuario(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tus datos han sido actualizados con éxito!')
            return redirect('perfil')
    else:
        form = UserChangeForm(instance=request.user)
        
    form.fields.pop('password', None)
    return render(request, 'perfil.html', {'form': form})

@login_required
def listar_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/listar.html', {'inmuebles': inmuebles})

# 1. Vista para crear un nuevo inmueble (Arrendadores)
@login_required
def crear_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.propietario = request.user  # Asignamos al usuario actual como propietario si aplica
            inmueble.save()
            messages.success(request, '¡Inmueble creado con éxito!')
            return redirect('listar_inmuebles')
    else:
        form = InmuebleForm()
    return render(request, 'inmuebles/form_inmueble.html', {'form': form, 'accion': 'Crear'})

# 2. Vista para actualizar un inmueble existente
@login_required
def actualizar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Inmueble actualizado con éxito!')
            return redirect('listar_inmuebles')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'inmuebles/form_inmueble.html', {'form': form, 'accion': 'Actualizar'})

# Vista adicional para eliminar inmueble
@login_required
def eliminar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.method == 'POST':
        inmueble.delete()
        messages.success(request, '¡Inmueble eliminado con éxito!')
        return redirect('listar_inmuebles')
    return render(request, 'inmuebles/confirmar_eliminar.html', {'inmueble': inmueble})