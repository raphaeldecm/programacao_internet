from django.urls import path

from . import views

app_name = "noticias"

urlpatterns = [
  # Categorias
  path("categoria/lista/", views.categorias_lista_view, name="categorias"),
  path("categoria/detalhe/<int:categoria_id>/", views.categoria_detalhe_view, name="categoria_detalhe"),
  # Tags
  path("tag/lista/", views.tags_lista_view, name="tags"),
  path("tag/detalhe/<int:tag_id>/", views.tag_detalhe_view, name="tag_detalhe"),
  # Notícias
  path("noticia/lista/", views.noticias_lista_view, name="noticias"),
  path("noticia/detalhe/<int:noticia_id>/", views.noticia_detalhe_view, name="noticia_detalhe"),
]