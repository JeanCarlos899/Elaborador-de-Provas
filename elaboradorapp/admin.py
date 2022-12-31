from django.contrib import admin
from .models import Question, Disciplina, Conteudo, Logo
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'conteudo', 'enunciado', 'dificuldade')
    list_filter = ('disciplina', 'conteudo', 'dificuldade', 'serie', 'criador__username')
    search_fields = ['enunciado', 'disciplina__nome', 'conteudo__nome', 'dificuldade', 'serie', 'vinculo__username', 'criador__username']
    fields = [
        'vinculo',
        'serie',
        'dificuldade',
        'disciplina',
        'conteudo',
        'enunciado',
        'imagem',
        'comando',
        'alternativa_a',
        'imagem_a',
        'alternativa_b',
        'imagem_b',
        'alternativa_c',
        'imagem_c',
        'alternativa_d',
        'imagem_d',
        'alternativa_e',
        'imagem_e',
        'gabarito',
    ]

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and obj.vinculo and obj.vinculo == request.user:
            return True
        if obj and obj.criador and obj.criador == request.user:
            return True
        if obj and obj.vinculo and obj.vinculo != request.user:
            return False
        if obj and obj.criador and obj.criador != request.user:
            return False
        return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and obj.vinculo and obj.vinculo == request.user:
            return True
        if obj and obj.criador and obj.criador == request.user:
            return True
        if obj and obj.vinculo and obj.vinculo != request.user:
            return False
        if obj and obj.criador and obj.criador != request.user:
            return False
        return False
    
    def save_model(self, request, obj, form, change):
        obj.criador = request.user
        super().save_model(request, obj, form, change)

class ConteudoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'disciplina']
    list_filter = ['disciplina']
    search_fields = ['nome', 'disciplina__nome']
    ordering = ['disciplina']

class MyUserAdmin(UserAdmin):

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    
    def get_model_perms(self, request):
        if request.user.is_superuser:
            return super().get_model_perms(request)
        return {}


class MyGroupAdmin(GroupAdmin):

    def get_model_perms(self, request):
        if request.user.is_superuser:
            return super().get_model_perms(request)
        return {}


admin.site.register(Question, QuestionAdmin)
admin.site.register(Disciplina)
admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Logo)
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, MyGroupAdmin)