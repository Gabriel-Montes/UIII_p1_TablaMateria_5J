from django.urls import path
from materia_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('regismaterias/',views.regismaterias,name='regismaterias'),
    path('borrarMat/<codigo>',views.borrarMat,name="borrarMat"),
    path('selecMat/<codigo>',views.selecMat,name='selecMat'),
    path('editMat/',views.editMat,name="editMat"),
]
