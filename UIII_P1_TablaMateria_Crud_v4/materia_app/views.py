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

def selecMat(request,codigo):
    mat=Materia.objects.get(codigo=codigo)
    return render(request,'editarMat.html',{"mmaterias":mat})

def editMat(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]
    mat=Materia.objects.get(codigo=codigo)
    mat.nombre=nombre
    mat.creditos=creditos
    mat.save()
    return redirect('/')


def borrarMat(request,codigo):
    mat=Materia.objects.get(codigo=codigo)
    mat.delete()
    return redirect('/')
