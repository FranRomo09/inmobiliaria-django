from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('propiedades.urls')),  # Todas las rutas de la app se incluyen aquí
    path('accounts/', include('django.contrib.auth.urls')),  # Para login/logout por defecto si los usas
]