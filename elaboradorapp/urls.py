from django.urls import path 
from . import views   

app_name = 'elaboradorapp'

urlpatterns = [
    path('', views.ElaboradorApp.as_view(), name='index'),
    path('listar-questoes/', views.QuestionsView.as_view(), name='listar-questoes'),
    path('sobre/', views.Sobre.as_view(), name='sobre'),
    path('salvar-prova/', views.save_prova, name='salvar-prova'),
    path('listar-provas/', views.ListarProvas.as_view(), name='listar-provas'),
    path('ver-prova/<int:id>', views.ver_prova, name='ver-prova'),
    path('deletar-prova/<int:id>', views.delete_prova, name='deletar-prova'),
]