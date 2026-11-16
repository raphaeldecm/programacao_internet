from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('cursos/', views.curso_lista, name='curso_lista'),
    path('cursos/novo/', views.curso_criar, name='curso_criar'),
    path('cursos/<int:pk>/', views.curso_detalhe, name='curso_detalhe'),
    path('cursos/<int:pk>/editar/', views.curso_editar, name='curso_editar'),
    path('cursos/<int:pk>/excluir/', views.curso_excluir, name='curso_excluir'),
]
