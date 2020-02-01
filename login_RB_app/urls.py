from django.urls import path
from login_RB_app import views

app_name = 'app'

urlpatterns = [
    path('lista', views.ListMikrotikView.as_view(),name='lista'),
    path('estatus/<int:pk>/', views.DetailMikrotikView.as_view(),name='estatus'),
    path('cadastro', views.CreateMikrotikView.as_view(),name='cadastro'),
    path('update/<int:pk>/', views.UpdateMikrotikView.as_view(),name='update'),
    path('delete/<int:pk>/', views.DeleteMikrotikView.as_view(),name='delete'),
    path('add_user_command', views.add_user_command,name='add_user_command'),
    path('update_user_command', views.update_user_command,name='update_user_command'),
    path('remove_user_command', views.remove_user_command,name='remove_user_command'),

]
