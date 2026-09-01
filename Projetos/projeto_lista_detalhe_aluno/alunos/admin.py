from django.contrib import admin

from .models import Aluno, Disciplina

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'email',
                    'data_nascimento',
                    'curso',
                    'periodo')
    search_fields = ('nome', )
    list_filter = ('curso', 'periodo')

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'professor') # Adiciona colunas na lista de disciplinas no admin
    search_fields = ('nome', 'codigo', 'professor') # Adiciona campos de pesquisa no admin para facilitar a busca por disciplinas

admin.site.register(Aluno, AlunoAdmin) # Registra o modelo Aluno no admin com a configuração personalizada AlunoAdmin
admin.site.register(Disciplina, DisciplinaAdmin)