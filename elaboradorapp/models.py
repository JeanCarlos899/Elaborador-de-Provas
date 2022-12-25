from django.db import models
from django.contrib.auth.models import User

difficulty_question = (
    ('F', 'Fácil'),
    ('M', 'Média'),
    ('D', 'Difícil'),
)

series = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)


alternativas = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
)

class Disciplina(models.Model): #country
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Conteudo(models.Model): #city
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Conteúdos'
        
class Logo(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField('imagem', upload_to='images/')

    def __str__(self):
        return self.nome


class Question(models.Model): 
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Vincular questão')
    serie = models.CharField('Série', max_length=100, choices = series, blank=True)
    dificuldade = models.CharField('Dificuldade', max_length = 5, choices = difficulty_question, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, verbose_name='Disciplina')
    conteudo = models.ForeignKey(Conteudo, on_delete=models.SET_NULL, null=True, verbose_name='Conteúdo')
    enunciado = models.TextField('Enunciado', max_length=5000)
    imagem = models.ImageField('Imagem', upload_to='images/', null=True, blank=True)
    comando = models.TextField('Comando', max_length=5000, null=True, blank=True)
    alternativa_a = models.TextField('Alternativa A', max_length=5000, null=True, blank=True)
    imagem_a = models.ImageField('Imagem A', upload_to='images/', null=True, blank=True)
    alternativa_b = models.TextField('Alternativa B', max_length=5000, null=True, blank=True)
    imagem_b = models.ImageField('Imagem B', upload_to='images/', null=True, blank=True)
    alternativa_c = models.TextField('Alternativa C', max_length=5000, null=True, blank=True)
    imagem_c = models.ImageField('Imagem C', upload_to='images/', null=True, blank=True)
    alternativa_d = models.TextField('Alternativa C', max_length=5000, null=True, blank=True)
    imagem_d = models.ImageField('Imagem D', upload_to='images/', null=True, blank=True)
    alternativa_e = models.TextField('Alternativa E', max_length=5000, null=True, blank=True)
    imagem_e = models.ImageField('Imagem E', upload_to='images/', null=True, blank=True)
    gabarito = models.CharField('Gabarito', max_length=5000, choices = alternativas)

    
    def __str__(self):
        return str(self.disciplina) + ' - ' + str(self.conteudo) + ' - ' + str(self.enunciado[:100]) + '...'
    
    class Meta:
        verbose_name = u'questão'
        verbose_name_plural = u'questões'
        ordering = ['disciplina', 'conteudo']
        