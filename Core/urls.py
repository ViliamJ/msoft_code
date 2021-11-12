from django.urls import path
from . import views

import Core.dash_apps.finished_apps.model_table
from Core.dash_apps import index
from Core.dash_apps import app

urlpatterns = [
    path('', views.home, name='home'),
    path('model/<str:model>/', views.ModelListView.as_view(), name='model_list'),
    path('model/<str:model>/detail/', views.model_detail, name='model_detail'),
    path('model/<str:model>/add/', views.model_add, name='model_add'),
    path('graph/', views.graph, name='graph'),
    path('accounts/user/', views.simple_user, name='user')

]