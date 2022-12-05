from django.views.generic import ListView
from .models import Question, Disciplina, Conteudo

class ElaboradorApp(ListView):
    model = Question
    template_name = 'elaboradorapp/index.html'
