from django.urls import path
from login_RB_app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastrar, name='cadastro'),
    path('estatus/id', views.estatus, name='estatus'),
]
