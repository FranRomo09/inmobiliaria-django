import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmobiliaria.settings')
django.setup()

from django.db import connection

def consultar_por_region():
    # Consulta SQL nativa uniendo Inmueble, Comuna y Región
    query = """
        SELECT r.nombre AS region, c.nombre AS comuna, i.nombre, i.descripcion 
        FROM propiedades_inmueble i
        JOIN propiedades_comuna c ON i.comuna_id = c.id
        JOIN propiedades_region r ON c.region_id = r.id
        ORDER BY r.nombre;
    """
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        resultados = cursor.fetchall()
        
    # Guardar resultados en un archivo de texto
    nombre_archivo = "inmuebles_por_region.txt"
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("=== REPORTE DE INMUEBLES POR REGIÓN ===\n\n")
        for fila in resultados:
            region, comuna, nombre, descripcion = fila
            archivo.write(f"Región: {region} | Comuna: {comuna}\n")
            archivo.write(f"  - Nombre: {nombre}\n")
            archivo.write(f"  - Descripción: {descripcion}\n")
            archivo.write("-" * 40 + "\n")
            
    print(f"Reporte generado con éxito en: {nombre_archivo}")

if __name__ == '__main__':
    consultar_por_region()