# Documentación del Proyecto: Hito 2 - Configuración del Admin de Django

## 1. Introducción
El propósito de este hito es configurar, registrar y personalizar el panel de administración de Django (`django.contrib.admin`) para la empresa inmobiliaria, permitiendo una gestión visual eficiente de las regiones, comunas, tipos de inmuebles y propiedades.

---

## 2. Creación del Superusuario (Requerimiento 1)
Para acceder al sistema de administración, se creó un usuario con privilegios totales mediante la terminal ejecutando el comando:

python manage.py createsuperuser

Se suministraron los datos correspondientes de nombre de usuario, correo electrónico y contraseña segura, los cuales quedaron almacenados en la base de datos de autenticación de Django.

3. Registro de Modelos en el Admin (Requerimiento 2)
Se estructuraron e incorporaron los modelos relacionales Region, Comuna, TipoInmueble e Inmueble en el archivo propiedades/models.py, asegurando las llaves foráneas correspondientes. Posteriormente, se importaron y registraron en propiedades/admin.py para hacerlos visibles en la interfaz gráfica del panel de control.

4. Personalización del Panel de Administración (Requerimiento 3)
Para mejorar la usabilidad y la experiencia de gestión de datos, se aplicaron las siguientes propiedades en las clases de administración (ModelAdmin):

list_display: Permite visualizar en forma de tabla las columnas clave de cada modelo (por ejemplo, nombre del inmueble, tipo, comuna, habitaciones y baños).

list_filter: Incorpora un panel lateral derecho de filtrado rápido por categorías como tipo de inmueble, región y comuna.

search_fields: Habilita una barra de búsqueda inteligente para filtrar registros por texto (nombre, dirección o descripción).


5. Generación del archivo de dependencias
Para asegurar la portabilidad y correcta ejecución del entorno, se actualizó el archivo de dependencias con el comando:

pip freeze > requirements.txt

![alt text](<Captura de pantalla 2026-10-04 a la(s) 6.25.31 p.m..png>)