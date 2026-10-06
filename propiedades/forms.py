from django import forms
from .models import Inmueble

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        # Excluimos temporalmente 'arrendatario' o lo manejamos en la vista si es necesario
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_totales', 
            'estacionamientos', 'habitaciones', 'bano', 'direccion', 
            'comuna', 'tipo_inmueble'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'm2_construidos': forms.NumberInput(attrs={'class': 'form-control'}),
            'm2_totales': forms.NumberInput(attrs={'class': 'form-control'}),
            'estacionamientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'bano': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-select'}),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-select'}),
        }