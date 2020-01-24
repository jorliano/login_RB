from django.urls import path
from login_RB_app import views

app_name = 'app'

urlpatterns = [
    path('lista', views.ListMikrotikView.as_view(),name='lista'),
    path('estatus/<int:pk>/', views.DetailMikrotikView.as_view(),name='estatus'),
    path('cadastro', views.CreateMikrotikView.as_view(),name='cadastro'),
    path('update/<int:pk>/', views.UpdateMikrotikView.as_view(),name='update'),
    path('delete/<int:pk>/', views.DeleteMikrotikView.as_view(),name='delete'),
    path('commands', views.add_user_command,name='commands'),

]
