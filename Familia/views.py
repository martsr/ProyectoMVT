from django.http import HttpResponse
from Familia.models import Familiar
from django.shortcuts import render


# Create your views here.
def carga_familiares(request, nombre, parentesco, edad, fecha_nac, foto_src=None):
    if foto_src is None:
        foto_src = "default.jpg"
    return HttpResponse(f"Familiar cargado: nombre: {nombre}, parentesco: {parentesco}, edad: {edad}, fecha_nac: {fecha_nac} , foto_src: {foto_src} ")


def vista_familiares(request):
    familiares = Familiar.objects.all().values()
    context = {'familiares': familiares}
    return render(request, "Familia/index.html", context)

