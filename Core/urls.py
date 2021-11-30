from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('model/<str:model>/', views.ModelListView.as_view(), name='model_list'),
    path('model/<str:model>/detail/', views.model_detail, name='model_detail'),
    path('model/<str:model>/add/', views.model_add, name='model_add'),
    path('createadmin/', views.create_admin, name='user'),
    path('delete/<str:object_id>/', views.delete, name='delete')
]
