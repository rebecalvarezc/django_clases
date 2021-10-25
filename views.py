from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
# from django.template.loader import get_template


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# contenido estático.
def primera_vista(request):  # a toda función creada dentro del archivo views.py se le denomina "vista"
    path = 'C:/Users/Rebeca/PycharmProjects/djangoProject/plantillas/plantilla1.html'
    # Esto idealmente se hace con cargadores.
    with open(path, 'r', encoding='utf-8') as doc_externo:
        plantilla = Template(doc_externo.read())  # ¿Por qué tengo que poner read dos veces?
    ctx = Context()
    doc = plantilla.render(ctx)
    return HttpResponse(doc)


# # Cargando las plantillas manualmente:
# def segunda_vista(request):
#     creador = Persona('Rebeca', 'Alvarez C')
#     path = 'C:/Users/Rebeca/PycharmProjects/djangoProject/plantillas/plantilla2.html'
#     now = datetime.datetime.now()
#     temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
#     with open(path, 'r', encoding='utf-8') as doc_externo:
#         plantilla = Template(doc_externo.read())
#     ctx = Context({'nombre_creador': creador.nombre, 'apellido_creador': creador.apellido, 'hora': now,
#                    'temas': temas_curso})
#     # podemos poner directamente la información en las key del dict o si usamos POO crear una clase y con sus atributos
#     # añadir información al dict
#     doc = plantilla.render(ctx)
#     return HttpResponse(doc)


# Usando cargadores:
def segunda_vista(request):
    now = datetime.datetime.now()
    temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    creador = Persona('Rebeca', 'Alvarez C')
    plantilla = loader.get_template('plantilla2.html')  # se pone la dirección de los templates en settings.py primero
    # este template no es igual al anterior, por lo que el render va a funcionar de forma diferente.
    doc = plantilla.render({'nombre_creador': creador.nombre, 'apellido_creador': creador.apellido, 'hora': now,
                            'temas': temas_curso})
    # al ser diferente el template anterior, se para el diccionario asi, no con un context
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
