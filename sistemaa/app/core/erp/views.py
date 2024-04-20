from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from core.erp.forms import CategoryForm
from django.utils.decorators import method_decorator  
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.views.decorators.csrf import csrf_exempt   
from django.http import JsonResponse, HttpResponseRedirect            
from core.erp.models import Category, Product                
from django.urls import reverse_lazy                    
from core.erp.forms import ProductForm                               


# Create your views here.
def home(request):
  

    return render(request, '/home/josev646/Documentos/proyecto/automatas2-Proyecto/sistemaa/app/core/erp/templates/index.html')


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
        return JsonResponse(data, safe=False)
    
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
    

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de una categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        return context
    

class CategoryFormView(FormView):
    form_class = CategoryForm
    template_name = 'create.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        print(form.is_valid())
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.is_valid())
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Categoria'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('category_list')
        context['action'] = 'add'
        return context
    

##############################################################################################################
class ProductListView(ListView):
    model = Product
    template_name = 'list_product.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('product_create')
        context['list_url'] = reverse_lazy('product_list')
        context['entity'] = 'Productos'
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'creaate_product.html'
    success_url = reverse_lazy('product_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('product_list')
        context['action'] = 'add'
        return context




class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'creaate_product.html'
    success_url = reverse_lazy('product_list')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('product_list')
        context['action'] = 'edit'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product_list')

    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('product_list')
        return context