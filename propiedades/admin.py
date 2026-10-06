from django.contrib import admin
from .models import Region, Comuna, TipoInmueble, Inmueble

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'region')
    list_filter = ('region',)
    search_fields = ('nombre',)

@admin.register(TipoInmueble)
class TipoInmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_inmueble', 'comuna', 'habitaciones', 'bano', 'm2_construidos')
    list_filter = ('tipo_inmueble', 'comuna', 'habitaciones')
    search_fields = ('nombre', 'direccion', 'descripcion')