from django.urls import path
from login_RB_app import views

app_name = 'app'

urlpatterns = [
    # path('', views.IndexView.as_view()),
    path('', views.ListMikrotikView.as_view(),name='lista'),
    path('estatus/<int:pk>/', views.DetailMikrotikView.as_view(),name='estatus'),
    path('cadastro', views.CreateMikrotikView.as_view(),name='cadastro'),
    path('update/<int:pk>/', views.UpdateMikrotikView.as_view(),name='update'),
    path('delete/<int:pk>/', views.DeleteMikrotikView.as_view(),name='delete'),


    path('adicionar/enviar_comando', views.AdicionarUserComandoView.as_view(),name='add_user_command'),
    path('atualizar/enviar_comando', views.AtualizarUserComandoView.as_view(),name='update_user_command'),
    path('remover/enviar_comando', views.RemoverUserComandoView.as_view(),name='remove_user_command'),
    path('resultado/comandos', views.ResutadoComandoView.as_view(),name='resultado_comandos'),


]
