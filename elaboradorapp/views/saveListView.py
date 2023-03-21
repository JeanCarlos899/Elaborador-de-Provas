from django.http import JsonResponse
from elaboradorapp.models import Prova
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import redirect
from django.db.models import Q
from bs4 import BeautifulSoup

class ListarProvas(ListView):
    model = Prova
    template_name = 'elaboradorapp/listar_provas.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redireciona o usuário para a página de login
            return redirect('/admin/login/?next=/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        provas = Prova.objects.all().filter(criador=self.request.user).order_by('-id')

        if self.request.GET.get('search_box'):
            search_box = self.request.GET['search_box']
            provas = Prova.objects.filter(Q(nome_prova__icontains=search_box) | Q(
                criador__username__iexact=search_box))

        context.update({
            'provas': provas,
        })

        return context


def save_prova(request):

    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/admin/login/?next=/')

    if request.method == 'POST':
        id = request.POST.get('id')
        html_prova = request.POST.get('html_prova')
        nome_prova = request.POST.get('nome_prova')
        html_prova = BeautifulSoup(html_prova, "html.parser").prettify()
        
        if id != '':
            if Prova.objects.filter(pk=id).exists():
                Prova.objects.filter(pk=id).update(
                    html_prova=html_prova, nome_prova=nome_prova)
            else:
                return JsonResponse({"status": "error", "message": "Prova não encontrada"})
        else:
            prova = Prova(html_prova=html_prova,
                          nome_prova=nome_prova, criador=request.user)
            prova.save()
        return JsonResponse({"status": "success"})


def ver_prova(request, id):
    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/admin/login/?next=/')

    user = request.user
    prova = Prova.objects.get(
        id=id,
        criador=user
    )
    return render(request, 'elaboradorapp/ver_prova.html', {'prova': prova})


def delete_prova(request, id):
    if not request.user.is_authenticated:
        # Redireciona o usuário para a página de login
        return redirect('/admin/login/?next=/')

    user = request.user
    prova = Prova.objects.get(
        id=id,
        criador=user
    )
    prova.delete()
    return redirect('elaboradorapp:listar-provas')
