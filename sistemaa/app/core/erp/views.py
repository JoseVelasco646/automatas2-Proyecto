from django.shortcuts import render
from core.erp.models import Category



# Create your views here.
def home(request):
  

    return render(request, '/home/josev646/Documentos/proyecto/automatas2-Proyecto/sistemaa/app/core/erp/templates/home.html')

def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }

    return render(request, 'list.html', data)