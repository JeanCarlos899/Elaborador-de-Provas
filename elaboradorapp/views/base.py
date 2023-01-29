from django.views.generic import ListView
from elaboradorapp.models import Question, Disciplina, Conteudo, Logo
from django.shortcuts import redirect

class ElaboradorApp(ListView):
    model = Question
    template_name = 'elaboradorapp/index.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redireciona o usuário para a página de login
            return redirect('/admin/login/?next=/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disciplinas'] = Disciplina.objects.all()
        context['conteudos'] = Conteudo.objects.all()
        context['logos'] = Logo.objects.all()
        context['nome_professor'] = self.request.user.first_name + ' ' + self.request.user.last_name
        return context

class Sobre(ListView):
    model = Question
    template_name = 'elaboradorapp/sobre.html'
