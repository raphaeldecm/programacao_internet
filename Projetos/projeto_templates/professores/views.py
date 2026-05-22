from django.shortcuts import render

# Create your views here.
def professores_list(request):
    return render(request, 'professores/list.html')