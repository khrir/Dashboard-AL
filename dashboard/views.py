from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Repasses_Municipios, Despesas_favorecidos, Despesas_Categoria_Economica

# Create your views here.
def home(request):
    return render(request, 'home.html')

def relatorio_repasses_municipios(request):
    repasses_municipios = Repasses_Municipios.objects.all()
    label = []
    data = []
    for repasse in repasses_municipios:
        label.append(repasse.nome)
        data.append(repasse.total)

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:10], 'data': x[1][:10]})

def relatorio_despesas_categoria_economica(request):
    despesas_categoria_economica = Despesas_Categoria_Economica.objects.all()
    label = []
    data = []
    for despesa in despesas_categoria_economica:
        label.append(despesa.nome)
        data.append(despesa.total)

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:10], 'data': x[1][:10]})

def relatorio_despesas_favorecidos(request):
    despesas_favorecidos = Despesas_favorecidos.objects.all()
    label = []
    data = []
    for despesa in despesas_favorecidos:
        label.append(despesa.nome)
        data.append(despesa.custeio)

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:10], 'data': x[1][:10]})
