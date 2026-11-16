from django.urls import path
from . import views

app_name = 'estudante'

urlpatterns = [
    path('estudantes/', views.estudante_lista, name='estudante_lista'),
    path('estudantes/novo/', views.estudante_criar, name='estudante_criar'),
    path('estudantes/<int:pk>/', views.estudante_detalhe, name='estudante_detalhe'),
    path('estudantes/<int:pk>/editar/', views.estudante_editar, name='estudante_editar'),
    path('estudantes/<int:pk>/excluir/', views.estudante_excluir, name='estudante_excluir'),
]
