import base64

from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html', {})

def login(request):

    # Extrae el nombre de ususario y la contraseña
    username, password = base64.b64decode(
        request.headers['Authorization'].split()[-1]
        ).decode("ascii").split(':')

    # Determina si el usuario existe
    user = auth.authenticate(request, username=username, password=password)
    
    # Inicia la sesión
    if user is not None:
        auth.login(request, user)
        return HttpResponse("Autenticación exitosa.\n")
    
    # Credenciales inválidas
    else:
        return HttpResponse("Las credenciales no son válidas.\n")

def logout(request):
    # Cierra la sesión
    auth.logout(request)
    return HttpResponse("La sesión fue cerrada.\n")
