from django.urls import path

from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.products_list, name='produtos'),
    path('create/', views.products_create, name='produtos-create'),
    path('update/', views.products_update, name='produtos-update'),
    path('detail/', views.products_detail, name='produtos-detail'),
]