from django.shortcuts import render
from .models import Materia

# Create your views here.
def index(request):
    lmaterias=Materia.objects.all()
    return render(request,'gestMateria.html',{'mmaterias':lmaterias})