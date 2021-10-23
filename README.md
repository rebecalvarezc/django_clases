## Lessons Learned:

1.- En el archivo de 'urls.py' se escriben las rutas de las páginas webs y además se les anexa las 'funciones' que se van a ejecutar en esa página.
2.- En un archcivo llamado 'views.py' se crean las funciones que se van a utilizar en la página web.
3.- Las plantillas contienen código html (entre otros) y son una buena práctica al usar Django.
4.- Para cargar las plantillas se usan cargadores, en donde en la función Context() se introduce un diccionario con las variables a usar en la plantilla.
Posteriormente, en la plantilla se escribe el valor a usar de la siguiente forma: {{Clave_dict}}.