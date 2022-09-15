from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def inicio(request):
    return render (request, 'AppTenis/inicio.html')

def sociostenis(request):
    return render (request, 'AppTenis/sociostenis.html')

def categoriatercera(request):
    return render (request, 'AppTenis/categoriatercera.html')

def categoriacuarta(request):
    return render (request, 'AppTenis/categoriacuarta.html')

def damas(request):
    return render (request, 'AppTenis/damas.html')

def asociate(request):
    return render (request, 'AppTenis/asociate.html')

def sociosFormulario(request):
    if request.method=='POST':
        form=SociosForm(request.POST)
        print('--------------')
        PRINT(form)
        print('--------------')
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion['nombre']
            apellido=informacion['apellido']
            edad=informacion['edad']
            email=informacion['email']
            socio = SociosTenis(nombre=nombre, apellido=apellido, edad=edad, email=email)
            socio.save()
            return render(request, 'AppTenis/inicio.html', {'mensaje': 'Socio creado'})

    else:
        formulario=SociosForm()
    return render(request, 'AppTenis/asociate.html', {'formulario':formulario})

