from typing import Any
from django.contrib.auth.views import LoginView

class LoginFormView(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'iniciar sesion'
        return contex