from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.request

# Create your views here.

CACHE = { }


def home(request): #PAGINA PRINCIPAL
    salida = "Bienvenido a X-Serv-App-Cache-Django, estas son las paginas disponibles hasta el momento: "
    return HttpResponse(salida)

@csrf_exempt
def pagina(request, pagina):

    if pagina in CACHE:
        return HttpResponse(CACHE[pagina])
    else:
        peticion = urllib.request.urlopen(pagina)
        CACHE[pagina] = peticion
        return HttpResponse(peticion)
