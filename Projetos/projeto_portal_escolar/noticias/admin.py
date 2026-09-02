from django.contrib import admin

# Register your models here.
from .models import Categoria, Tag, Noticia, Usuario, Perfil

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_publicacao', 'categoria')
    search_fields = ('titulo', 'texto')
    list_filter = ('categoria', 'tags')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    search_fields = ('nome', 'email')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'bio')
    search_fields = ('usuario__nome', 'bio')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Perfil, PerfilAdmin)