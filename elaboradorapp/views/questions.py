
# Módulo que contém a classe que gerencia a distribuição das questões 
# de acordo com a quantidade de conteúdos e a quantidade de questões

class GetQuestions:
    def __init__(self, qtd_conteudos, quantidade_questoes, questoes_primeiro_conteudo, questoes_segundo_conteudo, questoes_terceiro_conteudo):
        self.qtd_conteudos = qtd_conteudos
        self.quantidade_questoes = quantidade_questoes
        self.questoes_primeiro_conteudo = questoes_primeiro_conteudo
        self.questoes_segundo_conteudo = questoes_segundo_conteudo
        self.questoes_terceiro_conteudo = questoes_terceiro_conteudo

    def get_questions(self):

        if self.qtd_conteudos != 0 and (self.questoes_primeiro_conteudo or self.questoes_segundo_conteudo or self.questoes_terceiro_conteudo):
            
            # Se a quantidade de questões for divisível pela quantidade de conteúdos, então é possível distribuir igualmente
            # Se não for, então é atribuida mais uma questão do primeiro conteúdo (o principal)

            qtd_questoes = self.quantidade_questoes
            qtd_conteudos = self.qtd_conteudos
            
            if int(self.quantidade_questoes) % self.qtd_conteudos == 0:

                if self.questoes_primeiro_conteudo:
                    self.quantidade_questoes = self.quantidade_questoes 

                    # Caso haja a questão do conteúdo, então é obtida uma fatia do queryset com a quantidade de questões
                    # dividida pela quantidade de conteúdos, através de uma divisão inteira

                    # O mesmo é feito para os conteúdos posteriores, caso existam

                    self.questoes_primeiro_conteudo = self.questoes_primeiro_conteudo.order_by('?')[:int(qtd_questoes) // qtd_conteudos]
                if self.questoes_segundo_conteudo:
                    self.questoes_segundo_conteudo = self.questoes_segundo_conteudo.order_by('?')[:int(qtd_questoes) // qtd_conteudos]
                if self.questoes_terceiro_conteudo:
                    self.questoes_terceiro_conteudo = self.questoes_terceiro_conteudo.order_by('?')[:int(qtd_questoes) // qtd_conteudos]
            else:

                # Caso a quantidade de questões não seja divisível pela quantidade de conteúdos, então é atribuida mais uma
                # questão do primeiro conteúdo (o principal)

                if self.questoes_primeiro_conteudo:
                    self.questoes_primeiro_conteudo = self.questoes_primeiro_conteudo.order_by('?')[:int(qtd_questoes) // qtd_conteudos + 1]
                if self.questoes_segundo_conteudo:
                    self.questoes_segundo_conteudo = self.questoes_segundo_conteudo.order_by('?')[:int(qtd_questoes) // qtd_conteudos]
                if self.questoes_terceiro_conteudo:
                    self.questoes_terceiro_conteudo = self.questoes_terceiro_conteudo.order_by('?')[:int(qtd_questoes) // qtd_conteudos]
            

            # Após a distribuição das questões, é feita a união dos querysets, para que seja possível retornar um único queryset
            if self.questoes_primeiro_conteudo:
                questoes = self.questoes_primeiro_conteudo
            if self.questoes_segundo_conteudo:
                # Se já houver questões do primeiro conteúdo, então é feita a união com as questões do segundo conteúdo
                if self.questoes_primeiro_conteudo:
                    questoes = questoes | self.questoes_segundo_conteudo
                else:
                    questoes = self.questoes_segundo_conteudo
            if self.questoes_terceiro_conteudo:
                # Se já houver questões do primeiro ou segundo conteúdo, então é feita a união com as questões do terceiro conteúdo
                if self.questoes_primeiro_conteudo or self.questoes_segundo_conteudo:
                    questoes = questoes | self.questoes_terceiro_conteudo
                else:
                    questoes = self.questoes_terceiro_conteudo

            return questoes