from django.urls import path
from login_RB_app import views

app_name = 'app'

urlpatterns = [
    path('lista', views.ListMikrotikView.as_view(),name='lista'),
    path('cadastro', views.CreateMikrotikView.as_view(),name='cadastro'),
    path('estatus/<int:pk>/', views.DetailMikrotikView.as_view(),name='estatus'),
    path('update/<int:pk>/', views.UpdateMikrotikView.as_view(),name='update'),
    path('delete/<int:pk>/', views.DeleteMikrotikView.as_view(),name='delete'),


]
