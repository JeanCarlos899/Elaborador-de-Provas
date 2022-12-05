from django.views.generic import ListView
from .models import Question, Disciplina, Conteudo

class ElaboradorApp(ListView):
    model = Question
    template_name = 'elaboradorapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(ElaboradorApp, self).get_context_data(**kwargs)
        return context