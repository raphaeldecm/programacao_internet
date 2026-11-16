from django.core.management.base import BaseCommand
from django.db import transaction

from noticias.models import Categoria, Noticia, Tag


CATEGORIAS = ("Eventos", "Educação", "Esportes", "Tecnologia", "Comunicados")
TAGS = ("Escola", "Alunos", "Professores", "Comunidade", "Projetos", "Inscrições")
NOTICIAS = (
    (
        "Feira de ciências reúne projetos dos alunos",
        "A escola realizará uma feira de ciências com experimentos e trabalhos "
        "desenvolvidos em sala de aula. As famílias estão convidadas a participar.",
        "Eventos",
        ("Alunos", "Comunidade", "Projetos"),
    ),
    (
        "Biblioteca promove semana de incentivo à leitura",
        "A biblioteca preparou rodas de leitura e atividades de troca de livros. "
        "Os alunos poderão compartilhar suas histórias favoritas com as turmas.",
        "Educação",
        ("Escola", "Alunos", "Professores"),
    ),
    (
        "Inscrições abertas para o campeonato escolar",
        "Os estudantes interessados em participar do campeonato escolar devem "
        "procurar os professores de educação física para inscrever suas equipes.",
        "Esportes",
        ("Alunos", "Inscrições"),
    ),
    (
        "Oficina de programação apresenta desafios de lógica",
        "O laboratório de informática receberá uma oficina de programação. "
        "Os participantes criarão pequenos projetos e resolverão desafios em equipe.",
        "Tecnologia",
        ("Alunos", "Professores", "Projetos"),
    ),
    (
        "Reunião de responsáveis discutirá o planejamento escolar",
        "A equipe pedagógica convida os responsáveis para conhecer o planejamento "
        "das atividades e conversar sobre o acompanhamento dos estudantes.",
        "Comunicados",
        ("Escola", "Comunidade"),
    ),
    (
        "Mostra cultural valoriza os talentos da comunidade",
        "A mostra cultural contará com apresentações musicais, exposições de arte "
        "e trabalhos produzidos pelas turmas ao longo do período letivo.",
        "Eventos",
        ("Escola", "Comunidade", "Projetos"),
    ),
)


class Command(BaseCommand):
    help = "Popula categorias, tags e notícias de exemplo sem duplicar os dados."

    @transaction.atomic
    def handle(self, *args, **options):
        categorias = {}
        categorias_criadas = 0
        for nome in CATEGORIAS:
            categoria, criada = Categoria.objects.get_or_create(nome=nome)
            categorias[nome] = categoria
            categorias_criadas += criada

        tags = {}
        tags_criadas = 0
        for nome in TAGS:
            tag, criada = Tag.objects.get_or_create(nome=nome)
            tags[nome] = tag
            tags_criadas += criada

        noticias_criadas = 0
        for titulo, texto, categoria, nomes_tags in NOTICIAS:
            noticia, criada = Noticia.objects.get_or_create(
                titulo=titulo,
                defaults={"texto": texto, "categoria": categorias[categoria]},
            )
            if criada:
                noticia.tags.set([tags[nome] for nome in nomes_tags])
                noticias_criadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Dados criados: {categorias_criadas} categorias, "
                f"{tags_criadas} tags e {noticias_criadas} notícias."
            )
        )
