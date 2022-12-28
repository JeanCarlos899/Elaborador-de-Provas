from django.views.generic import ListView
from elaboradorapp.models import Question, Disciplina, Conteudo, Logo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class ElaboradorApp:
    def __init__(self):
        self.disciplinas = Disciplina.objects.all()
        self.conteudos = Conteudo.objects.all()
        self.logos = Logo.objects.all()

    @login_required(login_url='/admin/')
    def index(request):
        return render(request, 'elaboradorapp/index.html', {
            'disciplinas': Disciplina.objects.all(),
            'conteudos': Conteudo.objects.all(),
            'logos': Logo.objects.all(),
        })

class Sobre(ListView):
    model = Question
    template_name = 'elaboradorapp/sobre.html'