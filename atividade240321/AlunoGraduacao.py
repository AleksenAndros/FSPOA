from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, cod, nome, matricula, semestre):
        Aluno.__init__(self, cod, nome, matricula)
        self.semestre = semestre
        
    def imprimir(self):
        Aluno.imprimir(self)
        print('        {}º Semestre Graduação'.format(self.semestre))