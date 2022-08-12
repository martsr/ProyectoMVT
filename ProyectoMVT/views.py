from django.http import HttpResponse
from django.template import Template, Context 
def datos(request):
    return HttpResponse("Working")

def template_test(self):
    miHtml=open('/Users/martina/Documents/Coder/ProyectoMVT/ProyectoMVT/templates/template1.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto=Context()
    doc=plantilla.render(miContexto)
    return HttpResponse(doc)