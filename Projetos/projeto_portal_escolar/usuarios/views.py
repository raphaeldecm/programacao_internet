from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UsuarioForm


# Create your views here.
def cadastrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect("login")
        else:
            messages.error(request, "Erro ao cadastrar usuário. Verifique os dados e tente novamente.")
    else:
        form = UsuarioForm()
    return render(request, "registration/cadastro.html", {"form": form})