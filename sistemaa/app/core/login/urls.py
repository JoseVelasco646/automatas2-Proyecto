from django.urls import path

from core.login.views import *

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('login/logout/', LogoutView.as_view(), name='logout')

    


]