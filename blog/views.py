from django.shortcuts import render

def list_carro(request):
    return render(request, 'blog/list_carro.html', {})
