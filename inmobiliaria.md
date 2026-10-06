Documentación del Proyecto: Hito 1 - Inmobiliaria y Conexión a Base de Datos
1. Introducción y Requisitos Previos
El objetivo de este proyecto es desarrollar un sitio web para una empresa de arriendo de inmuebles, implementando una arquitectura robusta basada en Django y PostgreSQL.

Para la puesta en marcha del entorno de desarrollo se cumplieron los siguientes pasos técnicos:

Instalación de PostgreSQL: Configurado como motor relacional de base de datos para almacenar la información de los inmuebles y tipos de propiedades.

Entorno Virtual de Python: Se creó y activó un entorno virtual (env_inmobiliaria) para aislar las dependencias del proyecto.

Instalación de Paquetes: Se instalaron los paquetes necesarios utilizando el gestor pip:

Bash
pip install django psycopg2-binary
2. Creación del Proyecto y Aplicación
Se inicializó el proyecto principal de Django y la aplicación encargada de gestionar los modelos inmobiliarios:

Creación del proyecto: django-admin startproject inmobiliaria

Creación de la aplicación: python manage.py startapp propiedades

Configuración en settings.py: Se registró la aplicación 'propiedades' en la lista INSTALLED_APPS y se estableció la conexión a la base de datos PostgreSQL (db_inmobiliaria).

3. Definición del Modelo de Datos (Modelos y Relaciones)
En el archivo propiedades/models.py se definieron los modelos relacionales para representar el negocio, incorporando llaves primarias y una llave foránea (ForeignKey) para vincular los inmuebles con su respectiva categoría:

Modelo TipoInmueble: Almacena la categoría de la propiedad (ej. Casa, Departamento, Parcela).

Modelo Inmueble: Almacena el detalle de la propiedad (nombre, descripción, metros cuadrados, cantidad de habitaciones, baños, estacionamientos, dirección) y se relaciona mediante una llave foránea (ForeignKey) con TipoInmueble utilizando borrado en cascada (on_delete=models.CASCADE).

4. Implementación y Pruebas de Operaciones CRUD
Las operaciones de manipulación de datos se probaron y validaron interactivamente mediante la shell de Django (python manage.py shell), cumpliendo con los siguientes procedimientos:

Creación de registros (Create):

Se creó un registro en TipoInmueble (ej. "Departamento").

Se creó un registro en Inmueble asociado al tipo anterior ingresando sus metros cuadrados, ubicación y especificaciones.

Listado de registros (Read):

Se consultaron todos los registros almacenados utilizando el ORM de Django (Inmueble.objects.all()).

Actualización de registros (Update):

Se recuperó un inmueble específico por su ID y se modificaron atributos particulares (por ejemplo, la cantidad de estacionamientos), guardando los cambios con el método .save().

Eliminación de registros (Delete):

Se seleccionó un registro mediante su llave primaria y se ejecutó el método .delete() para removerlo de la base de datos de manera exitosa.

5. Conclusión
El sistema quedó configurado e integrado correctamente con PostgreSQL. Los modelos relacionales responden de forma óptima a las reglas de negocio solicitadas, y las pruebas ejecutadas desde la consola validan el correcto funcionamiento del ORM de Django para las operaciones CRUD.