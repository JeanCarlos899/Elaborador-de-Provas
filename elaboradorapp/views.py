from django.views.generic import ListView, View
# from elaboradorapp.utils import GeraPDFMixin
from .models import Question, Disciplina, Conteudo


class ElaboradorApp(ListView):
    model = Question
    template_name = 'elaboradorapp/index.html'

    def get_context_data(self, **kwargs):
        global disciplina_escolhida
        global conteudo_escolhido
        global serie_escolhida
        global dificuldade_escolhida
       
        context = super(ElaboradorApp, self).get_context_data(**kwargs)
        context['disciplinas'] = Disciplina.objects.all()
        context['conteudos'] = Conteudo.objects.all()

        disciplina_escolhida = self.request.GET.get('disciplina_value')
        conteudo_escolhido = self.request.GET.get('conteudo_value')
        serie_escolhida = self.request.GET.get('serie_value')
        dificuldade_escolhida = self.request.GET.get('dificuldade_value')

        return context

class ListarQuestoes(ListView):
    model = Question
    template_name = 'elaboradorapp/listar_questoes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questoes = Question.objects.all()
        conteudo = Conteudo.objects.filter(name=conteudo_escolhido)
        disciplina = Disciplina.objects.filter(name=disciplina_escolhida)

        conteudo = conteudo[0].pk
        disciplina = disciplina[0].pk

        if disciplina:
            questoes = Question.objects.filter(disciplina=disciplina, conteudo=conteudo, serie=serie_escolhida, dificuldade=dificuldade_escolhida)

        context.update({
            'questoes': questoes,
        })
        return context


# class ListarQuestoesPDF(View, GeraPDFMixin):
#     def get(self, request, *args, **kwargs):
#         questoes = Question.objects.all()
        
