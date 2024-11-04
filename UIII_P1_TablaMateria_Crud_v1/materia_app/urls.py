from django.urls import path
from materia_app import views

urlpatterns = [
    path('',views.index,name='index')
]
