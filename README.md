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

15.- Con la clase Model de Django creamos la base de datos, sin embargo para poder usarlo es necesario haber creado una aplicación.
(Django no puede trabajar con Modelos si no has creado una aplicación).

16.- Mediante el comando "python manage.py startapp 'nombredelaapp'" en el terminal, creamos la aplicación.
