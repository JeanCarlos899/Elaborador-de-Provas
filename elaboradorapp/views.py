from django.views.generic import ListView, View
from elaboradorapp.utils import GeraPDFMixin
from .models import Question, Disciplina, Conteudo
from django.db.models import Q

class ElaboradorApp(ListView):
    model = Question
    template_name = 'elaboradorapp/index.html'

    def get_context_data(self, **kwargs):
        context = super(ElaboradorApp, self).get_context_data(**kwargs)
        context['disciplinas'] = Disciplina.objects.all()
        context['conteudos'] = Conteudo.objects.all()
        return context

class ListarQuestoes(ListView):
    model = Question
    template_name = 'elaboradorapp/listar_questoes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questoes = Question.objects.all()

        disciplina = self.request.GET.get('disciplina_value')
        conteudo = self.request.GET.get('conteudo_value')
        serie = self.request.GET.get('serie_value')
        dificuldade = self.request.GET.get('dificuldade_value')

        if disciplina:
            questoes = Question.objects.filter(Q(disciplina__icontains=disciplina) & Q(conteudo__icontains=conteudo) & Q(serie__icontains=serie) & Q(dificuldade__icontains=dificuldade))
            print("tem disciplina")
        
        context.update({
            'questoes': questoes,
        
        })
        return context


class ListarQuestoesPDF(View, GeraPDFMixin):
    def get(self, request, *args, **kwargs):
        questoes = Question.objects.all()
        
