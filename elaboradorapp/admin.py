from django.contrib import admin

# Register your models here.

from .models import Question, Disciplina, Conteudo, Logo

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'conteudo', 'enunciado', 'dificuldade')
    list_filter = ('disciplina', 'conteudo', 'dificuldade', 'serie', 'autor__username')
    search_fields = ('enunciado', 'disciplina__nome', 'conteudo__nome', 'dificuldade', 'serie', 'autor__username')

class ConteudoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'disciplina']
    list_filter = ['disciplina']
    search_fields = ['nome', 'disciplina__nome']
    ordering = ['disciplina']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Disciplina)
admin.site.register(Conteudo, ConteudoAdmin)
admin.site.register(Logo)