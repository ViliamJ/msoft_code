from django.urls import path
from .views import dashboard_view
from .dash_apps import index
from .dash_apps import app


urlpatterns = [
    path('index/', dashboard_view),
]