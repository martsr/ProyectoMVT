from django.urls import path
from Familia.views import carga_familiares, vista_familiares

urlpatterns = [
    path('carga_familiares/<nombre>/<parentesco>/<edad>/<fecha_nac>', carga_familiares),
    path('vista_familiares/', vista_familiares),
]
