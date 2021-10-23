## Lessons Learned:

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
7.- Las llamadas a métodos desde una plantilla de python no usan los paréntesis. Ej: {{nombre.lower}}