from django.http import HttpResponse
import datetime
from django.template import Template, Context


# contenido estático.
def primera_vista(request):  # a toda función creada dentro del archivo views.py se le denomina "vista"
    path = 'C:/Users/Rebeca/PycharmProjects/djangoProject/plantillas/plantilla1.html'
    # Esto idealmente se hace con cargadores.
    with open(path, 'r', encoding='utf-8') as doc_externo:
        plantilla = Template(doc_externo.read())  # ¿Por qué tengo que poner read dos veces?
    ctx = Context()
    doc = plantilla.render(ctx)
    return HttpResponse(doc)


# Usando cargadores:
def segunda_vista(request):
    path = 'C:/Users/Rebeca/PycharmProjects/djangoProject/plantillas/plantilla2.html'
    with open(path, 'r', encoding='utf-8') as doc_externo:
        plantilla = Template(doc_externo.read())
    ctx = Context({'nombre_creador': 'Rebeca', 'apellido_creador': 'Alvarez'})
    doc = plantilla.render(ctx)
    return HttpResponse(doc)


# contenido dinámico
def fecha(request):
    fecha_actual = datetime.datetime.now()
    formato = """
    <html>
    <body>
        <h2> 
        La fecha y hora actual es: {}
        </h2>
    </body>
    </html>"""
    return HttpResponse(formato.format(fecha_actual))


# Django usa URL friendly, evita usar símbolos extraños en la URL.
def calculo_edad(request, year, edad):
    periodo = year - 2021
    edad_futura = edad + periodo
    formato = """
    <html>
    <body>
        <h2>
        En el año {} tendrás {} años.
        </h2>
    </body>
    </html>"""
    return HttpResponse(formato.format(year, edad_futura))

# Plantillas: se usan para separas la parte lógica de la parte visual de una web.
# Para usarlas: Creamos un objeto de tipo Template, crear un contexto
# (datos adicionales de la plantilla. Ej.: cont. dinámico), finalmente renderizar el objeto template.
