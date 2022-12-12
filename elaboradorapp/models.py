from django.db import models

difficulty_question = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
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
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Conteudo(models.Model): #city
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Question(models.Model): 
    serie = models.CharField('Serie', max_length=100, choices = series, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.SET_NULL, null=True)
    dificuldade = models.CharField('Dificuldade', max_length = 5, choices = difficulty_question, blank=True)
    enunciado = models.TextField('Enunciado', max_length=5000)
    imagem = models.ImageField('imagem', upload_to='images/', null=True, blank=True)
    comando = models.TextField('Comando', max_length=5000, null=True, blank=True)
    alternativa_a = models.TextField('Alternativa_a', max_length=5000, null=True, blank=True)
    imagem_a = models.ImageField('Imagem_a', upload_to='images/', null=True, blank=True)
    alternativa_b = models.TextField('Alternativa_b', max_length=5000, null=True, blank=True)
    imagem_b = models.ImageField('Imagem_b', upload_to='images/', null=True, blank=True)
    alternativa_c = models.TextField('Alternativa_c', max_length=5000, null=True, blank=True)
    imagem_c = models.ImageField('Imagem_c', upload_to='images/', null=True, blank=True)
    alternativa_d = models.TextField('Alternativa_d', max_length=5000, null=True, blank=True)
    imagem_d = models.ImageField('Imagem_d', upload_to='images/', null=True, blank=True)
    alternativa_e = models.TextField('Alternativa_e', max_length=5000, null=True, blank=True)
    imagem_e = models.ImageField('Imagem_e', upload_to='images/', null=True, blank=True)
    gabarito = models.CharField('Gabarito', max_length=5000, choices = alternativas)
    
    
    def __str__(self):
        return str(self.disciplina) + ' - ' + str(self.conteudo) + ' - ' + str(self.enunciado[:100]) + '...'




