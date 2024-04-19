from typing import Any
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('category_list')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'iniciar sesion'
        return contex
    