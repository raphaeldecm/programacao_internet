from django.urls import path

from .views import home_produtos

app_name = 'produtos'

urlpatterns = [
    path('', home_produtos, name='produtos'),
]