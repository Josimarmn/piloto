
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')
#view exibir_item
def exibir_item(request_id):
    return render (request, "exibir_item.html", {'id':id})