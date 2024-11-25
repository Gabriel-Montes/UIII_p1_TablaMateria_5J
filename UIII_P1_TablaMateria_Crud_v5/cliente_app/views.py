from django.shortcuts import render,redirect
from .models import Cliente

# Create your views here.
def index_Clientes(request):
    nclientes=Cliente.objects.all()
    return render(request,'gestCliente.html',{'mclientes':nclientes})

def regisClientes(request): 
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    edad=request.POST["numedad"]
    inst=request.POST["txtins"]
    direcc=request.POST["txtdirec"]
    exper=request.POST["txtexper"]
    
    guarCliente=Cliente.objects.create(
            id_cliente=id,nombre=nombre,edad=edad,intrumento=inst,direccion=direcc,experiencia=exper
    )
    return redirect("cliente")

def selecCli(request,id):
    cli=Cliente.objects.get(id_cliente=id)
    return render(request,'editarCli.html',{"mclientes":cli})

def editCli(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    edad=request.POST["numedad"]
    inst=request.POST["txtins"]
    direcc=request.POST["txtdirec"]
    exper=request.POST["txtexper"]
    cli=Cliente.objects.get(id_cliente=id)
    cli.nombre=nombre
    cli.edad=edad
    cli.intrumento=inst
    cli.direccion=direcc
    cli.experiencia=exper
    cli.save()
    return redirect('cliente')

def borrarCli(request,id):
    cli=Cliente.objects.get(id_cliente=id)
    cli.delete()
    return redirect('cliente')