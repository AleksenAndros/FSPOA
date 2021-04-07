class Aluno:
    def __init__(self, cod = None, nome = None, matricula = None):
        self.codigo = cod
        self.nome = nome
        self.matricula = matricula
    
    def imprimir(self):
        print('''
        Código: {}
        Nome: {}
        Matricula: {}'''.format(self.codigo, self.nome, self.matricula))