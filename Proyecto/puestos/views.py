from django.shortcuts import render
from puestos.models import Puesto

# Create your views here.
def puestos(request):
    puestos = Puesto.objects.all()
    return render(request, "puestos/puestos.html",{"puestos": puestos})