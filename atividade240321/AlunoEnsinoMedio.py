from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        Aluno.imprimir(self)
        print('        {}º ano Ensino Médio'.format(self.ano))