from django.urls import path

from . import views

app_name = 'professores'

urlpatterns = [
    path('', views.professores_list, name='professores_list'),
]