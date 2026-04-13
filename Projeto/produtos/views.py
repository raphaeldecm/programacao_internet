from django.shortcuts import render

# Create your views here.
def home_produtos(request):
    return render(request, 'produtos/home.html')