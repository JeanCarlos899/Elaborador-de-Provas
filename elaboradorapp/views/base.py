from django.views.generic import ListView
from elaboradorapp.models import Question, Disciplina, Conteudo, Logo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class ElaboradorApp:
    
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