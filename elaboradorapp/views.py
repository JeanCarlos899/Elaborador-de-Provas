from django.views.generic import ListView
from .models import Question, Disciplina, Conteudo
import datetime


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
        
        global questoes 

        disciplina_escolhida = self.request.GET.get('disciplina')
        quantidade_questoes = self.request.GET.get('quantidade_questoes')
        conteudo_escolhido = self.request.GET.get('conteudo')
        segundo_conteudo = self.request.GET.get('segundo_conteudo')
        terceiro_conteudo = self.request.GET.get('terceiro_conteudo')
        serie_escolhida = self.request.GET.get('serie')
        dificuldade_escolhida = self.request.GET.get('dificuldade')
        nome_professor = self.request.GET.get('nome_professor')
        curso = self.request.GET.get('curso')
        turma = self.request.GET.get('turma')
        data = self.request.GET.get('data')
        observacao_1 = self.request.GET.get('observacao_1')
        observacao_2 = self.request.GET.get('observacao_2')
        observacao_3 = self.request.GET.get('observacao_3')
        logo_url = self.request.GET.get('logo_url')
        

        context = super().get_context_data(**kwargs)
        questoes = Question.objects.all()

        conteudo = Conteudo.objects.filter(name=conteudo_escolhido)
        segundo_conteudo = Conteudo.objects.filter(name=segundo_conteudo)
        terceiro_conteudo = Conteudo.objects.filter(name=terceiro_conteudo)
        disciplina = Disciplina.objects.filter(name=disciplina_escolhida)
        
        try:
            conteudo = conteudo[0].pk
            disciplina = disciplina[0].pk
        except:
            conteudo = None
            disciplina = None
        try:
            segundo_conteudo = segundo_conteudo[0].pk
        except:
            segundo_conteudo = None
        try:
            terceiro_conteudo = terceiro_conteudo[0].pk
        except:
            terceiro_conteudo = None
            
        if serie_escolhida == 'Indefinido':
            questoes = Question.objects.filter(disciplina=disciplina, conteudo=conteudo, dificuldade=dificuldade_escolhida)
            if segundo_conteudo:
                questoes_segundo_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=segundo_conteudo, dificuldade=dificuldade_escolhida)
                questoes = questoes | questoes_segundo_conteudo
            if terceiro_conteudo:
                questoes_terceiro_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=terceiro_conteudo, dificuldade=dificuldade_escolhida)
                questoes = questoes | questoes_terceiro_conteudo
        if dificuldade_escolhida == 'Indefinido':
            questoes = Question.objects.filter(disciplina=disciplina, conteudo=conteudo, serie=serie_escolhida)
            if segundo_conteudo:
                questoes_segundo_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=segundo_conteudo, serie=serie_escolhida)
                questoes = questoes | questoes_segundo_conteudo
            if terceiro_conteudo:
                questoes_terceiro_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=terceiro_conteudo, serie=serie_escolhida)
                questoes = questoes | questoes_terceiro_conteudo
        if dificuldade_escolhida and serie_escolhida == 'Indefinido':
            questoes = Question.objects.filter(disciplina=disciplina, conteudo=conteudo)
            if segundo_conteudo:
                questoes_segundo_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=segundo_conteudo)
                questoes = questoes | questoes_segundo_conteudo
            if terceiro_conteudo:
                questoes_terceiro_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=terceiro_conteudo)
                questoes = questoes | questoes_terceiro_conteudo
        if serie_escolhida == 'Indefinido' and dificuldade_escolhida == 'Indefinido':
            questoes = Question.objects.filter(disciplina=disciplina, conteudo=conteudo)
            if segundo_conteudo:
                questoes_segundo_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=segundo_conteudo)
                questoes = questoes | questoes_segundo_conteudo
            if terceiro_conteudo:
                questoes_terceiro_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=terceiro_conteudo)
                questoes = questoes | questoes_terceiro_conteudo
        if dificuldade_escolhida != 'Indefinido' and serie_escolhida != 'Indefinido':
            questoes = Question.objects.filter(disciplina=disciplina, conteudo=conteudo, serie=serie_escolhida, dificuldade=dificuldade_escolhida)
            if segundo_conteudo:
                questoes_segundo_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=segundo_conteudo, serie=serie_escolhida, dificuldade=dificuldade_escolhida)
                questoes = questoes | questoes_segundo_conteudo
            if terceiro_conteudo:
                questoes_terceiro_conteudo = Question.objects.filter(disciplina=disciplina, conteudo=terceiro_conteudo, serie=serie_escolhida, dificuldade=dificuldade_escolhida)
                questoes = questoes | questoes_terceiro_conteudo
        if data:
            data = datetime.datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')

        questoes = questoes.order_by('?')[:int(quantidade_questoes)]

        context.update({
            'questoes': questoes,
            'nome_disciplina': disciplina_escolhida,
            'nome_conteudo': conteudo_escolhido,
            'nome_professor': nome_professor,
            'observacao1': observacao_1,
            'observacao2': observacao_2,
            'observacao3': observacao_3,
            'curso': curso,
            'turma': turma,
            'data': data,
            'logo_url': logo_url,
        })

        questoes = context
        
        return context

class Sobre(ListView):
    model = Question
    template_name = 'elaboradorapp/sobre.html'