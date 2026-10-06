from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')

    def __str__(self):
        return self.nombre

class TipoInmueble(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Inmueble(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construidos = models.IntegerField()
    m2_totales = models.IntegerField()
    estacionamientos = models.IntegerField(default=0)
    habitaciones = models.IntegerField(default=1)
    bano = models.IntegerField(default=1)
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, related_name='inmuebles')
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, related_name='inmuebles')

    def __str__(self):
        return self.nombre