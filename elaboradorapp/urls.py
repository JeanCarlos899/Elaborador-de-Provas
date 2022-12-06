from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
from . import views   

app_name = 'elaboradorapp'

urlpatterns = [
    path('', views.ElaboradorApp.as_view(), name='index'),
    path('listar_questoes/', views.ListarQuestoes.as_view(), name='listar_questoes'),
]