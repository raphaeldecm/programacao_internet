from django.urls import path

from . import views

app_name = "noticias"

urlpatterns = [
  path("categoria/lista/", views.categorias_lista_view, name="categorias"),
  path("categoria/detalhe/<int:categoria_id>/", views.categoria_detalhe_view, name="categoria_detalhe"),

]