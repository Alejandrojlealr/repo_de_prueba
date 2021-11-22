from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

from .models import Curso

# Create your views here.

def crear_curso(request): #se hizo un cambio para probar commit en github, se agrego 1 al nombre dela funcion
    curso = Curso(nombre='prueba', camada=5)
    curso.save()
    
    return HttpResponse(f'{curso.nombre} {curso.camada}')

# def ver_curso(request):
#     cursos = Curso.objects.all()
#     curso = cursos.last()
    
#     return HttpResponse(f'{curso.nombre}')

def ver_curso(request):
    cursos = Curso.objects.all()
    
    texto =' '
    for curso in cursos:
        texto += f'Curso: {curso.nombre} <br>'
    
    return HttpResponse(f'{texto}')


def prueba_template(request):
    # template = loader.get_template('Appcoder/index.html')*
    # documento = template.render({})*
    # return HttpResponse(documento)*
    #* Se comentan estas lineas para probar otra manera de cargar el template
    return render(request, 'Appcoder/index.html', {}) #ESTA LINEA ES OTRA MANERA PARA CARGAR EL TEMPLATE
