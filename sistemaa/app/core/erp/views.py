from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from core.erp.forms import CategoryForm
from django.utils.decorators import method_decorator  
from django.views.generic import ListView, CreateView, UpdateView
from django.views.decorators.csrf import csrf_exempt   
from django.http import JsonResponse, HttpResponseRedirect            
from core.erp.models import Category                   
from django.urls import reverse_lazy                                                   


# Create your views here.
def home(request):
  

    return render(request, '/home/josev646/Documentos/proyecto/automatas2-Proyecto/sistemaa/app/core/erp/templates/home.html')

def category_list(request):
    data = {
        'title': 'Listado de Categorias',
        'categories': Category.objects.all()
    }

    return render(request, 'list2.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'list2.html'

    @method_decorator (csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('category_create')
        context['list_url'] = reverse_lazy('category_list')
        context['entity'] = 'Categorias'
        return context
    
class CategoryCreateView(CreateView):

    model = Category
    form_class = CategoryForm
    template_name = 'create.html'
    success_url = reverse_lazy('category_list')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        return context
    

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create.html'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Categorías'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'edit'
        return context