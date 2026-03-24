from django.urls import path

from .views import home_blog, sobre, contato

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
]
