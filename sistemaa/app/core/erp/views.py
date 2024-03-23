from django.shortcuts import render


# Create your views here.
def home(request):
    data = {
        'name': 'jose'
    }

    return render(request, '/home/josev646/Documentos/sistemaa/app/core/erp/templates/index.html', data)