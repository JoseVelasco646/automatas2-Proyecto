"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.erp.views import *
from core.login.views import *
from django.conf import settings
from django.conf.urls.static import static
from core.erp.sale.views import SaleCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homee'),
    path('category/list2',CategoryListView.as_view(), name='category_list2'),
    path('category/list', category_list, name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    path('login/', include('core.login.urls')),
#####################Producto###################
    path('product/list', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
#####################clientes##########################
    path('client/list', clientes_list, name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='create_client'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),



    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
