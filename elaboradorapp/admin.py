from django.contrib import admin

# Register your models here.

from .models import Question, Disciplina, Conteudo

admin.site.register(Question)
admin.site.register(Disciplina)
admin.site.register(Conteudo)