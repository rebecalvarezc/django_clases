from django.http import HttpResponse
import datetime
from django.template import Template, Context


# contenido estático.
def primera_vista(request):  # a toda función creada dentro del archivo views.py se le denomina "vista"
    path = 'C:/Users/Rebeca/PycharmProjects/djangoProject/plantillas/plantilla1.html'
    # Esto idealmente se hace con cargadores.
    doc_externo = open(path, encoding='utf-8') # Intenté hacer esto con context manager pero no funcionó. Help :(
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    doc = plantilla.render(ctx)
    return HttpResponse(doc)


def segunda_vista(request):
    return HttpResponse('Hasta luego, gracias por visitar!')


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
