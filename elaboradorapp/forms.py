from django import forms
from .models import Question, Conteudo

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'disciplina',
            'serie',
            'gabarito',
            'conteudo',
            'dificuldade',
            'enunciado',
            'alternativa_a',
            'alternativa_b',
            'alternativa_c',
            'alternativa_d',
            'alternativa_e',
        ]