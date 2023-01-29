from django.db import models
from django.contrib.auth.models import User

class Disciplina(models.Model): 
    nome = models.CharField(max_length=30)
    criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Conteudo(models.Model): 
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)
    criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Conteúdos'
        
class Logo(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField('imagem', upload_to='images/')
    criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Question(models.Model): 

    vinculo = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        null=True,
        blank=True, 
        verbose_name='Vínculo'
    )

    serie = models.CharField(
        'série', 
        max_length=100, 
        blank=True,
        choices = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
        )
    )

    dificuldade = models.CharField(
        'dificuldade', 
        max_length = 5, 
        blank=True,
        choices = (
            ('F', 'Fácil'),
            ('M', 'Média'),
            ('D', 'Difícil')
        )
    )

    disciplina = models.ForeignKey(
        Disciplina, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='disciplina'
    )
    
    conteudo = models.ForeignKey(
        Conteudo, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='conteúdo'
    )

    enunciado = models.TextField(
        'enunciado', 
        max_length=5000
    )

    imagem = models.ImageField(
        'imagem', 
        upload_to='images/', 
        null=True, 
        blank=True
    )
    
    comando = models.TextField(
        'comando', 
        max_length=5000, 
        null=True, 
        blank=True
    )

    alternativa_a = models.TextField(
        'alternativa A',
        max_length=5000, 
        null=True, 
        blank=True
    )

    imagem_a = models.ImageField(
        'imagem A',
        upload_to='images/',
        null=True,
        blank=True
    )

    alternativa_b = models.TextField(
        'alternativa B',
        max_length=5000,
        null=True,
        blank=True
    )

    imagem_b = models.ImageField(
        'imagem B',
        upload_to='images/',
        null=True,
        blank=True
    )

    alternativa_c = models.TextField(
        'alternativa C',
        max_length=5000,
        null=True,
        blank=True
    )

    imagem_c = models.ImageField(
        'imagem C',
        upload_to='images/',
        null=True,
        blank=True
    )

    alternativa_d = models.TextField(
        'alternativa C',
        max_length=5000,
        null=True,
        blank=True
    )

    imagem_d = models.ImageField(
        'imagem D',
        upload_to='images/',
        null=True,
        blank=True
    )

    alternativa_e = models.TextField(
        'alternativa E',
        max_length=5000,
        null=True,
        blank=True
    )

    imagem_e = models.ImageField(
        'imagem E',
        upload_to='images/',
        null=True,
        blank=True
    )
    
    gabarito = models.CharField(
        'gabarito',
        max_length=5000, 
        blank=True,
        choices = (    
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E')
        ) 
    )

    criador = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='criador',
        related_name='criador'
    )

    def __str__(self):
        return (
            str(self.disciplina) + 
            ' - ' + 
            str(self.conteudo) + 
            ' - ' +
            str(self.enunciado[:100]) + 
            '...'
            )
    
    class Meta:
        verbose_name = u'questão'
        verbose_name_plural = u'questões'
        ordering = ['disciplina', 'conteudo']

class Prova(models.Model):
    html_prova = models.TextField()
    nome_prova = models.CharField(max_length=100, null=True, blank=True)
    criador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome_prova