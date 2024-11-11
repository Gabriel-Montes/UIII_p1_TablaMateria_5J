from django.shortcuts import render,redirect
from .models import Materia

# Create your views here.
def index(request):
    lmaterias=Materia.objects.all()
    return render(request,'gestMateria.html',{'mmaterias':lmaterias})

def regismaterias(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    guarmateria=Materia.objects.create(
        codigo=codigo,nombre=nombre,creditos=creditos
    )
    return redirect("/")