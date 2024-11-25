from django.urls import path
from cliente_app import views

urlpatterns = [
    path('clientes',views.index_Clientes,name='clientes'),
    path('regisClientes/',views.regisClientes,name='regisClientes'),
    path('selecCli/<id>',views.selecCli,name="selecCli"),
    path('editCli/<id>',views.editCli,name="editCli"),
    path('borrarCli/<id>',views.borrarCli,name="borrarCli"),
]
