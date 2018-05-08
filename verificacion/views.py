from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('verificacion/index.html')
    context = {
        'palabras': ['Hola', 'Adios']
    }
    return HttpResponse(template.render(context, request))