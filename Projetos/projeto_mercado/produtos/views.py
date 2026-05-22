from django.shortcuts import render

# Create your views here.
def products_list(request):
    return render(request, 'produtos/list.html')

def products_create(request):
    return render(request, 'produtos/form.html')

def products_update(request):
    return render(request, 'produtos/form.html')

def products_detail(request):
    return render(request, 'produtos/detail.html')