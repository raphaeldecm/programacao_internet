from django.urls import path
from .views import cadastrar_usuario

app_name = "usuarios"

urlpatterns = [
    path("cadastrar/", cadastrar_usuario, name="cadastrar_usuario"),
]