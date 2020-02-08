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


    path('add_user_command', views.AddUserCommandtView.as_view(),name='add_user_command'),
    path('update_user_command', views.UpdateUserCommandtView.as_view(),name='update_user_command'),
    path('remove_user_command', views.RemoveUserCommandtView.as_view(),name='remove_user_command'),
    path('resultado_comandos', views.ResutadoComandoView.as_view(),name='resultado_comandos'),


]
