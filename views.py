from django.http import HttpResponse
import datetime


# contenido estático.
def primera_vista(request):  # a toda función creada dentro del archivo views.py se le denomina "vista"
    return HttpResponse('<html><body><h1> Bienvenido a mi primera página con Django :) </h1></body></html>')


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