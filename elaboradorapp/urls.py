from django.urls import path 
from . import views   

app_name = 'elaboradorapp'

urlpatterns = [
    path('', views.ElaboradorApp.index, name='index'),
    path('listar_questoes/', views.QuestionsView.as_view(), name='listar_questoes'),
    path('sobre/', views.Sobre.as_view(), name='sobre'),
]