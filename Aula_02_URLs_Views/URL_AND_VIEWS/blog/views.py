from django.shortcuts import render

# Create your views here.
def home_blog(request):
    return render(request, 'blog/home.html')

def sobre(request):
    return render(request, 'blog/sobre.html')

def contato(request):
    return render(request, 'blog/contato.html')
