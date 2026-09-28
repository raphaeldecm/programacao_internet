from django.urls import path

from . import views

app_name = "noticias"

urlpatterns = [
  # Categorias
  path("categoria/lista/", views.categorias_lista_view, name="categorias"),
  path("categoria/detalhe/<int:categoria_id>/", views.categoria_detalhe_view, name="categoria_detalhe"),
  path("categoria/criar/", views.categoria_create_view, name="categoria_create"),
  path("categoria/editar/<int:categoria_id>/", views.categoria_update_view, name="categoria_update"),
  path("categoria/deletar/<int:categoria_id>/", views.categoria_delete_view, name="categoria_delete"),
  # Tags
  path("tag/lista/", views.tags_lista_view, name="tags"),
  path("tag/detalhe/<int:tag_id>/", views.tag_detalhe_view, name="tag_detalhe"),
  path("tag/criar/", views.tag_create_view, name="tag_create"),
  path("tag/editar/<int:tag_id>/", views.tag_update_view, name="tag_update"),
  path("tag/deletar/<int:tag_id>/", views.tag_delete_view, name="tag_delete"),
  # Notícias
  path("noticia/lista/", views.noticias_lista_view, name="noticias"),
  path("noticia/detalhe/<int:noticia_id>/", views.noticia_detalhe_view, name="noticia_detalhe"),
  path("noticia/criar/", views.noticia_create_view, name="noticia_create"),
  path("noticia/editar/<int:noticia_id>/", views.noticia_update_view, name="noticia_update"),
  path("noticia/deletar/<int:noticia_id>/", views.noticia_delete_view, name="noticia_delete"),
]