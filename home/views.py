
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')
#view exibir_item

def exibir_item(request, id):
    return render (request, "exibir_item.html", {'id':id})

def perfil(request, usuario):
    return render (request, "perfil.html", {'usuario':usuario})

def diadasemana(request, dia):   
    dias = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado"
    }
    if dia in dias:
        return HttpResponse(f"O dia correpondente é: {dias[dia]}")
    else:
        return HttpResponse("Dia inválido")
       

