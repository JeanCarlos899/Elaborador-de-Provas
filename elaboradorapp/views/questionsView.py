from django.views.generic import ListView
from elaboradorapp.models import Question, Disciplina, Conteudo, Logo
from django.db.models import Q
import datetime
from .questions import GetQuestions

class QuestionsView(ListView):
    model = Question
    template_name = 'elaboradorapp/listar_questoes.html'

    def get_userId(self):
        if self.request.user.is_authenticated:
            return int(self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Dados da prova que serão exibidos no cabeçalho
        context['nome_professor'] = self.request.GET.get('nome_professor')
        context['tipo_prova'] = self.request.GET.get('tipo_prova')
        context['observacao1'] = self.request.GET.get('observacao_1')
        context['observacao2'] = self.request.GET.get('observacao_2')
        context['observacao3'] = self.request.GET.get('observacao_3')
        context['curso'] = self.request.GET.get('curso')
        context['turma'] = self.request.GET.get('turma')
        context['bimestre'] = self.request.GET.get('bimestre')

        # Dados da prova que serão usados para filtrar as questões
        disciplina_escolhida = self.request.GET.get('disciplina')
        quantidade_questoes = self.request.GET.get('quantidade_questoes')
        conteudo_escolhido = self.request.GET.get('conteudo')
        segundo_conteudo = self.request.GET.get('segundo_conteudo')
        terceiro_conteudo = self.request.GET.get('terceiro_conteudo')
        serie_escolhida = self.request.GET.get('serie')
        dificuldade_escolhida = self.request.GET.get('dificuldade')
        nome_logo = self.request.GET.get('nome_logo')

        # Filtrando os valores e recebendo o primeiro objeto da lista
        conteudo = Conteudo.objects.filter(nome=conteudo_escolhido).first() 
        segundo_conteudo = Conteudo.objects.filter(nome=segundo_conteudo).first()
        terceiro_conteudo = Conteudo.objects.filter(nome=terceiro_conteudo).first()
        disciplina = Disciplina.objects.filter(nome=disciplina_escolhida).first()
        logo = Logo.objects.filter(nome=nome_logo).first().imagem.url
        
        # Verificando se os valores são nulos e se sim, atribuindo o valor da chave primária
        if conteudo:
            conteudo = conteudo.pk
        if segundo_conteudo:
            segundo_conteudo = segundo_conteudo.pk
        if terceiro_conteudo:
            terceiro_conteudo = terceiro_conteudo.pk
        if disciplina:
            disciplina = disciplina.pk

        # Dicionário que armazenará as questões filtradas
        dictionary_questions = {
            'primeiro_conteudo': Question.objects.filter(

                # Filtrando as questões pela disciplina e conteúdo, que é
                # comum a todos os filtros. No entanto, o segunto filtro é 
                # feito de acordo com suas particularidades

                disciplina=disciplina, 
                conteudo=conteudo, 
            ).filter(

                # Filtrando as questões pela série e dificuldade, que são
                # opcionais. Caso não sejam selecionados, não serão filtrados.
                # Sendo passado uma filtro vazio, o django não será alterado

                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(dificuldade=dificuldade_escolhida) if dificuldade_escolhida != 'Indefinido' else Q(),

                # Se o vinculo (atributo de Question) for igual ao usuário
                # logado ou igual a None, a questão será exibida
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'faceis_primeiro_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=conteudo,
                dificuldade='F'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'medias_primeiro_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=conteudo,
                dificuldade='M'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'dificeis_primeiro_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=conteudo,
                dificuldade='D'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'segundo_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=segundo_conteudo,
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(dificuldade=dificuldade_escolhida) if dificuldade_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'faceis_segundo_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=segundo_conteudo,
                dificuldade='F'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'medias_segundo_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=segundo_conteudo,
                dificuldade='M'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'dificeis_segundo_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=segundo_conteudo,
                dificuldade='D'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'terceiro_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=terceiro_conteudo,
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(dificuldade=dificuldade_escolhida) if dificuldade_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'faceis_terceiro_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=terceiro_conteudo,
                dificuldade='F'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'medias_terceiro_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=terceiro_conteudo,
                dificuldade='M'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
            'dificeis_terceiro_conteudo': Question.objects.filter(
                disciplina=disciplina,
                conteudo=terceiro_conteudo,
                dificuldade='D'
            ).filter(
                Q(serie=serie_escolhida) if serie_escolhida != 'Indefinido' else Q(),
                Q(vinculo=self.get_userId()) | Q(vinculo=None)
            ).order_by('?'),
        }

        # Inicializando as variáveis que serão utilizadas para armazenar as questões
        # Isso é necessário para que não ocorra erro de variável não definida caso
        # os valores recebidos pelo dicionário dejam vazios, ocasionando a não incialização
        # das variáveis

        questoes_primeiro_conteudo = None
        questoes_segundo_conteudo = None
        questoes_terceiro_conteudo = None

        # Verificando se foi selecionado uma dificuldade, pois se não for, não é necessário
        # filtrar as questões por dificuldade
        
        if dificuldade_escolhida != 'Indefinido':
            qtd_conteudos = 0

            # Verificando se foi selecionado um conteúdo
            if dictionary_questions['primeiro_conteudo']:
                if dificuldade_escolhida == 'F':

                    # Se a dificuldade escolhida for F (fácil), as questões do primeiro conteúdo
                    # serão as questões fáceis do primeiro conteúdo e 50% das questões médias do 
                    # primeiro conteúdo, ordenadas aleatoriamente e armazenadas na variável

                    # O mesmo é feito para as seleções de questões posteriores (segundo e terceiro 
                    # conteúdo), e também para as seleções de questões de dificuldade média e difícil

                    questoes_primeiro_conteudo = (
                        dictionary_questions['primeiro_conteudo'] | # Unindo as questões do primeiro conteúdo
                        dictionary_questions['medias_primeiro_conteudo'].order_by('?')[ 
                            :int(
                                len(dictionary_questions['medias_primeiro_conteudo']) * 0.5
                            )
                        ] 
                    ).order_by('?') # Ordenando aleatoriamente
                elif dificuldade_escolhida == 'M':
                    questoes_primeiro_conteudo = (
                        dictionary_questions['primeiro_conteudo'] | 
                        dictionary_questions['dificeis_primeiro_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['dificeis_primeiro_conteudo']) * 0.5
                                )
                            ] | 
                        dictionary_questions['faceis_primeiro_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['faceis_primeiro_conteudo']) * 0.5
                            )
                        ]
                    ).order_by('?')
                elif dificuldade_escolhida == 'D':
                    questoes_primeiro_conteudo = (
                        dictionary_questions['primeiro_conteudo'] | 
                        dictionary_questions['medias_primeiro_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['medias_primeiro_conteudo']) * 0.5
                            )
                        ]
                    ).order_by('?')
                qtd_conteudos += 1
            
            if dictionary_questions['segundo_conteudo']:
                if dificuldade_escolhida == 'F':
                    questoes_segundo_conteudo = (
                        dictionary_questions['segundo_conteudo'] | 
                        dictionary_questions['medias_segundo_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['medias_segundo_conteudo']) * 0.5
                            )
                        ]
                    ).order_by('?')    
                elif dificuldade_escolhida == 'M':
                    questoes_segundo_conteudo = (
                        dictionary_questions['segundo_conteudo'] | 
                        dictionary_questions['dificeis_segundo_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['dificeis_segundo_conteudo']) * 0.5
                            )
                        ] | 
                        dictionary_questions['faceis_segundo_conteudo'].order_by('?')[
                            :int(len(dictionary_questions['faceis_segundo_conteudo']) * 0.5
                            )
                        ]
                    ).order_by('?')    
                elif dificuldade_escolhida == 'D':
                    questoes_segundo_conteudo = (
                        dictionary_questions['segundo_conteudo'] | 
                        dictionary_questions['medias_segundo_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['medias_segundo_conteudo']) * 0.5
                            )
                        ]
                    ).order_by('?')
                qtd_conteudos += 1

            if dictionary_questions['terceiro_conteudo']:
                if dificuldade_escolhida == 'F':
                    questoes_terceiro_conteudo = (
                        dictionary_questions['terceiro_conteudo'] | 
                        dictionary_questions['medias_terceiro_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['medias_terceiro_conteudo']) * 0.5
                            )
                        ]
                    ).order_by('?')
                elif dificuldade_escolhida == 'M':
                    questoes_terceiro_conteudo = (
                        dictionary_questions['terceiro_conteudo'] | 
                        dictionary_questions['dificeis_terceiro_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['dificeis_terceiro_conteudo']) * 0.5
                            )
                        ] | 
                        dictionary_questions['faceis_terceiro_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['faceis_terceiro_conteudo']) * 0.5
                            )
                        ]
                    ).order_by('?')
                elif dificuldade_escolhida == 'D':
                    questoes_terceiro_conteudo = (
                        dictionary_questions['terceiro_conteudo'] | 
                        dictionary_questions['medias_terceiro_conteudo'].order_by('?')[
                            :int(
                                len(dictionary_questions['medias_terceiro_conteudo']) * 0.5
                            )
                        ]
                    ).order_by('?')
                qtd_conteudos += 1

            # Aqui é feita a chamada da função que irá retornar as questões de acordo com a quantidade
            # de conteúdos escolhidos e a quantidade de questões que o usuário deseja
            
            questions = GetQuestions(
                qtd_conteudos, 
                quantidade_questoes, 
                questoes_primeiro_conteudo, 
                questoes_segundo_conteudo, 
                questoes_terceiro_conteudo
            ).get_questions()

        else:

            # Aqui é feita basicamente o mesmo que o bloco de código acima, porém sem a
            # necessidade de filtrar a dificuldade e randomizar as questões de acordo
            # com a dificuldade escolhida

            qtd_conteudos = 0
            if dictionary_questions['primeiro_conteudo']:
                questoes_primeiro_conteudo = dictionary_questions['primeiro_conteudo']
                questoes_primeiro_conteudo = questoes_primeiro_conteudo.order_by('?')
                qtd_conteudos += 1
            if dictionary_questions['segundo_conteudo']:
                questoes_segundo_conteudo = dictionary_questions['segundo_conteudo']
                questoes_segundo_conteudo = questoes_segundo_conteudo.order_by('?')
                qtd_conteudos += 1
            if dictionary_questions['terceiro_conteudo']:
                questoes_terceiro_conteudo = dictionary_questions['terceiro_conteudo']
                questoes_terceiro_conteudo = questoes_terceiro_conteudo.order_by('?')
                qtd_conteudos += 1

            questions = GetQuestions(
                qtd_conteudos, 
                quantidade_questoes, 
                questoes_primeiro_conteudo, 
                questoes_segundo_conteudo, 
                questoes_terceiro_conteudo
            ).get_questions()

        # Recebendo o valor da data escolhida pelo usuário
        data = self.request.GET.get('data')

        # Verificando se a data foi escolhida
        if data:
            # Transformando ela para o padrão brasileiro
            data = datetime.datetime.strptime(data, '%Y-%m-%d').strftime('%d/%m/%Y')

        # Atualizando os valores processados no contexto
        context.update({
            'questoes': questions,
            'nome_disciplina': disciplina_escolhida,
            'nome_conteudo': conteudo_escolhido,
            'data': data,
            'logo': logo,
        })

        return context