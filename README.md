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

*Nota: ORM (Object Relational Mapping) es un modelo de programación que permite mapear las estructuras de una base de datos relacional sobre una estructura lógica de entidades con el objeto de simplificar y acelerar el desarrollo de nuestras aplicaciones.
Los ORMs tienden a “liberarnos” de la escritura o generación manual de código SQL. Así, los objetos o entidades de la base de datos virtual creada en nuestro ORM podrán ser manipulados por medio de algún lenguaje de nuestro interés según el tipo de ORM utilizado.

15.- Con la clase Model de Django creamos la base de datos, sin embargo para poder usarlo es necesario haber creado una aplicación.
(Django no puede trabajar con Modelos si no has creado una aplicación).

16.- Mediante el comando "python manage.py startapp 'nombredelaapp'" en el terminal, creamos la aplicación. Una vez creada la aplicación,
es necesario indicarle al proyecto que la misma existe en settings.py, en INSTALLED APPS.

17.- Una vez escritas las tablas de models, en el terminal: 'python manage.py makemigrations'. De esta forma creamos la base de datos y le indica a Django que debería de tener la misma dentro.
Sin embargo, en este punto no ha creado las tablas aún. Para ello debemos escribir en el terminal: 'python manage.py sqlmigratep "nombredelaapp" nro.delamigración'. El nro de la migración es el que nos ha dado anteriormente al usar
el comando 'makemigrations'.

18.-Las tablas que tiene Django tienen por defecto una Primary key que se Autoincrementa y es el 'id'. Para que finalmente esta base de datos tenga sus tablas usar en el terminal: 'python manage.py migrate'.

19.- Para manipular las bases de datos: 'python manage.py shell' ---> Veremos el shell porque vemos: >>> en el terminal. Con esto:

    a) Luego debemos importar el modelo con el que vamos a trabajar.
    'from "nombreproyecto".models import "modeloconelquevamosatrabajar"'. Ejm: 'from manage_orders.models import Orders'.

    b) Para insertar valores en la tabla: variable = Modelo(colum1='info', columna2= 000). Nota: el texto va en comillas simples pero los números no.
    Ejm.: goods = Goods(name='table', section='decorations', prince=100) (lo mismo quue decir INSERT INTO table VALUES...). Para guardar los cambios: variable.save().

    c) Se puede hacer sin tantos pasos mediante: 'variable = Modelo.objects.create(colum1='info', colum2=000)'. De esta forma se crea el artículo sin usar el save().

    d) Para actualizar un artículo en la tabla: 'variableasignada.columna = nuevo valor', posteriormente usamos variableasignada.save().
    Ejm: goods.price=95, goods.save(). (Lo mismo que un query de tipo UPDATE)
    
    e) Para eliminar una fila: creamos una variable nueva --> variablenueva= Modelo.objects.get(criterio) y luego usar: variablenueva.delete()
    
    f) Para realizar un SELECT: variablenueva = Modelo.objects.all(), esto almacena todos los artículos que tengo en mi variable nueva.
    
20.- Para configurar Django con PostgreSQL:

    a) En la página principal, descargar el gestor de base de datos.
    b) Crear la contraseña que nos va a pedir PostgreSQL para manejarlo.
    c) En la base de datos que crea SQL por defecto (postgres): botón derecho -> query tool. Aquí podemos introducir instrucciones de tipo SQL.
    Ejm.: create database 'DataBaseName'.
    
    d) Para conectar la base de datos creada en PostgreSQL con Django es necesario instalar la libreria psycopg2 ('pip installs psycopg2').
    e) En settings.py en DATABASES cambiar: 'ENGINE' a: 'django.db.backends.postgreSQL_psycopg2' y 'NAME' a: 'DataBaseName'.
    Añadir al dict: 'USER': 'postgres', 'PASSWORD': 'contraseña', 'HOST': LocalHost (ó 127.0.0.1), 'DATABASE_PORT': '5432',.
    f) Posteriormente en el terminal: 'python manage.py makemigrations' y luego 'pythonn manage.py migrate'.
    g) Dentro de Schemes encontraremos las tablas creadas que se migraron de Django.

21.- Para manipular la base de datos de PostgreSQL:

    a) 'python manage.py shell'
    b) 'from "nombredelaapp".models import "NombreTabla"'
    c) client=Clients(name='Rebeca', address='My home', phone='12345678'), client.save()

22.- Como realizar consultas con criterios:
    
    a) 'python manage.py shell'
    b) 'from manage_orders.models import Goods'
    c) con clausula WHERE: 'Goods.objects.filter(criterio1, criterio2, ...). Esto nos devuelve un  QuerySet con dos objetos dentro de una lista.
    Para ver la información dentro de la lista hay que pedirle a Django que nos transforme los Modelos creados en cadenas de caracteres. 
    Para ello usamos: __str__ dentro de la clase creada (definimos la función).
    
    *Nota: siempre que hagamos cambios en la clase hay que volver a migrar (e importar y volver a hacer el comando de filter) para poder usar la clase actualizada.*
    
    d)- Para usar > y <: Goods.objects.filter(price__gte= numero) esto es equivalente a buscar un precio mayor que numero. Para menor que se usa: __lte=numero.
    Se puede usar tambien price__range(num1, num2) **IMPORTANTE: No me funciona, preguntar!!!**
    e) Para establecer ORDEY BY: Goods.objects.filter(criterio).order_by('columna') de forma ascendente, de forma descendente: .order_by('-colum').

23.- Un panel de administración maneja tu página web (de la misma forma que un gestor de contenidos (Ej. Wordpress) te ayuda a manejar el diseño de una página web)
desde un perfil de administrador. Dependiendo de la complejidad de la página es necesario usar este panel o no. Cuando creamos el proyecto con 'startproject' el panel de administración
de Django ya aparece habilitado. En urls.py está el path al panel de administración, es el primero de la lista.

    a) Para acceder al panel es necesario crear un superusuario, esto lo debemos hacer nosotros. En el terminal, dentro de la carpeta del proyecto, usar: 'python manage.py createsuperuser'.
    Nota: Las otras tablas que Django crea por defecto en las bases de datos están relacionadas a la información del panel de usuarios.

    b)En el archivo admin.py se codifica lo necesario para poder manipular nuestras tablas. Una vez codificado aquí, aparecerá la tabla en el panel de administración.
    De esta forma podemos manejar algunas tablas de una forma más friendly. 
    Nota: En el panel de administración, los campos que aparezcan en negritas serán aquellos que son obligatorios rellenar.

    c) Para hacer un campo opcional nos vamos a models.py y en el argumento del campo incluimos: blank=True, null=True. Ejm: models.CharField(blank=True, null=True).
    Luego tenemos que 'python manage.py makemigrations' & 'python manage.py migrate'.

    d) Para cambiar los nombres de los campos de las tablas en el panel de administración (no afectando la tabla), dentro del argumento del campo incluimos verbose_name="Nombre que queremos mostrar".
    Existe otra forma, pero puede generar problemas con las claves foráneas, por lo cual evitar usar un método diferente a este. 

    e)Si quiero ver más campos en el panel de administración, en el archivo admin creo una clase que herede de model admin (la cual permite hacer modificaciones en los modelos con los que estamos trabajando en el panel de administración).
    Para esto creamos una clase en admin.py y mediante el método list_display indicamos que campos quiero mostrar. Ejm.- list_display=('name', 'phone').
    Nota: en admin.site.register(Modelo, NuevaClase) --> Incluir la nueva clase que hereda en el comando. Luego tenemos que reiniciar el servidor.

    f) Para hacer búsquedas agregamos en la clase anterior el método search_fields = ('campo1', 'campo2'...).

    g) Para filtrar los registros de la tabla en el panel de administración en admin.py creamos una nueva clase, la cual heredará de 'admin.ModelAdmin' como la clase que creamos en el punto anterior.
    Dentro de la clase usar list_filters =().Actualizar también el admin.site.register de la tabla a fitrar. Además, si usamos date_hierarchy = 'campo1', me detecta los meses y días en donde tengo guardado registros.

24.- Para enviar datos al servidor usamos un request, el servidor puede manipular este objeto request y obtener a su vez información del usuario (IP, navegador utilizado, etc.)
Nota: Buscar request object Django y leer la documentación oficial.

25.- Se puede usar la información de un formulario para buscar en una base de datos, sin embargo, es necesario agregar parámetros a esta búsqueda para disminuir los recursos consumidos.

26.- Buscar CSRF token (impide ataque a la web por secuestro de sesión).

27.- Para enviar e-mail desde Django se hace uso de la librería core.mail.

    En settings.py introducir al final: EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    Nota: buscar esto en la documentación de Django.
    Luego: EMAIL_HOST = 'smtp.gmail.com'
    Nota: Gmail viene configurado para impedir a programas de terceros el uso de su mensajería. Si lo queremos usar en Django debemos cambiar la configuración del e-mail.
    
A continuación es necesario especificar el protocolo de seguridad que utilizan en el servidor de correos (TLS o SSL), dependiendo del utilizado es necesario usar un puerto u otro.
Esto también se encuentra en la configuración de gmail.

    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'dirección de correo eléctronico de gmail'
    EMAIL_HOST_PASSWORD = 'contraseña'

Posteriormente, si queremos probar que está funcionando lo configurado:

    >>> python manage.py shell
    >>> from django.core.mail import send_mail
    >>> send_mail('asunto del mensaje', 'cuerpo del mensaje', 'dirección del remitente', ['direccion del destinatario'], fail_silently= False)

Si todo está como queremos, en views.py hacemos la configuración de que se envíe la información del formulario al correo configurado.