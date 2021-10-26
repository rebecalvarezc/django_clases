## Lessons Learned:

0.- Un Framework es una estructura base utilizada como punto de partida para elaborar un proyecto con objetivos específicos.

1.- En el archivo de 'urls.py' se escriben las rutas de las páginas webs y además se les anexa las 'funciones' que se van a ejecutar en esa página.

2.- En un archivo llamado 'views.py' se crean las funciones que se van a utilizar en la página web.

3.- Las plantillas contienen código html (entre otros) y son una buena práctica al usar Django.

4.- Para cargar las plantillas se usan cargadores, en donde en la función Context() se introduce un diccionario con las variables a usar en la plantilla.
Posteriormente, en la plantilla se escribe el valor a usar de la siguiente forma: {{Clave_dict}}.

5.- Existe una jerarquía/ orden de llamadas desde las plantillas:
    
- Diccionarios
- Atributos
- Métodos
- Índice de lista

6.- Se puede hacer uso de bucles for en plantillas mediante el uso de corchetes simples. Ej.: {% for x in list %}.
Nota: es importante cerrar el bucle con: {% endfor %}. Además puede usarse también para los if y estos hay que cerrarlos también.

7.- Las llamadas a métodos desde una plantilla de python no usan los paréntesis. Ej: {{nombre.lower}}.

8.- Existen filtros de plantilla, que son como los métodos de Python.

9.- Es posible utilizar operadores de comparación dentro de los if de las plantillas, aunque debemos evitar abusar de esto.

10.- Las plantillas pueden incluir otras plantillas mediante: {% include "ruta/de/la/plantilla" %}.

11.- Al igual que en la POO se puede crear una plantilla padre de la que otras plantillas puedan heredar. La herencia se indica en cada 
plantilla mediante el uso de {% extends "Padre.html" %}.

12.- Django nos permite trabajar con bases de datos. Soporta oficialmente a: SQLite3 (Gestor por defecto), PostgreSQL (Recomendado), MySQL y Oracle.
Aunque puede usar otros.

13.- Django hace una diferencia entre un proyecto y una aplicación. La segunda forma parte de un proyecto y dependiendo de la complejidad del mismo,
puede tener más o menos aplicaciones. Las aplicaciones realizan una tarea (o suma de tareas) concretas.

14.- La modularidad es una propiedad que nos permitirá subdividir nuestro programa en partes más pequeñas (sub-programas) que habitualmente 
llamamos “módulos” las cuales deben ser independientes de la aplicación o programa original en sí. Esto es importante para poder reutilizar las aplicaciones en
distintos proyectos.

Nota: ORM (Object Relational Mapping) es un modelo de programación que permite mapear las estructuras de una base de datos relacional sobre una estructura lógica de entidades con el objeto de simplificar y acelerar el desarrollo de nuestras aplicaciones.
Los ORMs tienden a “liberarnos” de la escritura o generación manual de código SQL. Así, los objetos o entidades de la base de datos virtual creada en nuestro ORM podrán ser manipulados por medio de algún lenguaje de nuestro interés según el tipo de ORM utilizado.
Django utiliza este modelo para manejar sus bases de datos.

15.- Con la clase Model de Django creamos la base de datos, sin embargo para poder usarlo es necesario haber creado una aplicación.
(Django no puede trabajar con Modelos si no has creado una aplicación).

16.- Mediante el comando "python manage.py startapp 'nombredelaapp'" en el terminal, creamos la aplicación. Una vez creada la aplicación,
es necesario indicarle al proyecto que la misma existe en settings.py, en INSTALLED APPS.

17.- Una vez escritas las tablas de models, en el terminal: 'python manage.py makemigrations'. De esta forma creamos la base de datos y le indica a Django que debería de tener la misma dentro.
Sin embargo, en este punto no ha creado las tablas aún. Para ello debemos escribir en el terminal: 'python manage.py "nombredelaapp" nro.delamigración'. El nro de la migración es el que nos ha dado anteriormente al usar
el comando 'makemigrations'.

18.-Las tablas que tiene Django tienen por defecto una Primary key que se Autoincrementa y es el 'id'. Para que finalmente esta base de datos tenga sus tablas usar en el terminal: 'python manage.py migrate'.

19.- Para manipular las bases de datos: 'python manage.py shell' ---> Veremos el shell porque vemos: >>> en el terminal. Con esto:

    19.0.- Luego debemos importar el modelo con el que vamos a trabajar.
    'from "nombreproyecto".models import "modeloconelquevamosatrabajar"'. Ejm: 'from manage_orders.models import Orders'.

    19.1.- Para insertar valores en la tabla: variable = Modelo(colum1='info', columna2= 000). Nota: el texto va en comillas simples pero los números no.
    Ejm.: goods = Goods(name='table', section='decorations', prince=100) (lo mismo quue decir INSERT INTO table VALUES...). Para guardar los cambios: variable.save().

    19.2.- Se puede hacer sin tantos pasos mediante: 'variable = Modelo.objects.create(colum1='info', colum2=000)'. De esta forma se crea el artículo sin usar el save().

    19.3.- Para actualizar un artículo en la tabla: 'variableasignada.columna = nuevo valor', posteriormente usamos variableasignada.save().
    Ejm: goods.price=95, goods.save(). (Lo mismo que un query de tipo UPDATE)
    
    19.4.- Para eliminar una fila: creamos una variable nueva --> variablenueva= Modelo.objects.get(criterio) y luego usar: variablenueva.delete()
    
    19.5.- Para realizar un SELECT: variablenueva = Modelo.objects.all(), esto almacena todos los artículos que tengo en mi variable nueva.
    
20.- Para configurar Django con PostgreSQL:

    20.1.- En la página principal, descargar el gestor de base de datos.
    20.2.- Crear la contraseña que nos va a pedir PostgreSQL para manejarlo.
    20.3.- En la base de datos que crea SQL por defecto (postgres): botón derecho -> query tool. Aquí podemos introducir instrucciones de tipo SQL.
    Ejm.: create database 'DataBaseName'.
    20.4.- Para conectar la base de datos creada en PostgreSQL con Django es necesario instalar la libreria psycopg2 ('pip installs psycopg2').
    20.5.- En settings.py en DATABASES cambiar: 'ENGINE' a: 'django.db.backends.postgreSQL_psycopg2' y 'NAME' a: 'DataBaseName'.
    Añadir al dict: 'USER': 'postgres', 'PASSWORD': 'contraseña', 'HOST': LocalHost (ó 127.0.0.1), 'DATABASE_PORT': '5432',.
    20.6.- Posteriormente en el terminal: 'python manage.py makemigrations' y luego 'pythonn manage.py migrate'.
    20.7.- Dentro de Schemes encontraremos las tablas creadas que se migraron de Django.

21.- Para manipular la base de datos de PostgreSQL:

    21.1.- 'python manage.py shell'
    21.2.- 'from "nombredelaapp".models import "NombreTabla"'
    21.3.- client=Clients(name='Rebeca', address='My home', phone='12345678'), client.save()

22.- Como realizar consultas con criterios:
    
    22.0.- 'python manage.py shell'
    22.1.- 'from manage_orders.models import Goods'
    22.2.- con clausula WHERE: 'Goods.objects.filter(criterio1, criterio2, ...). Esto nos devuelve un  QuerySet con dos objetos dentro de una lista.
    Para ver la información dentro de la lista hay que pedirle a Django que nos transforme los Modelos creados en cadenas de caracteres. 
    Para ello usamos: __str__ dentro de la clase creada (definimos la función).
    Nota: siempre que hagamos cambios en la clase hay que volver a migrar (e importar y volver a hacer el comando de filter) para poder usar la clase actualizada.
    22.3.- Para usar > y <: Goods.objects.filter(price__gte= numero) esto es equivalente a buscar un precio mayor que numero. Para menor que se usa: __lte=numero.
    Se puede usar tambien price__range(num1, num2) IMPORTANTE: No me funciona, preguntar!!!
    22.4.- Para establecer ORDEY BY: Goods.objects.filter(criterio).order_by('columna') de forma ascendente, de forma descendente: .order_by('-colum').

