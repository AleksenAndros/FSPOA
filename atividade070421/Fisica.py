from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codFisica, nomeFisica, endFisica, cpf, idade, peso, altura, telefone = None):
        Pessoa.__init__(self, codFisica, nomeFisica, endFisica, telefone)
        self._cpf   = cpf
        self.idade  = idade
        self.peso   = peso
        self.altura = altura

    def imprimeCPF(self):
        Pessoa.printName(self)
        print(f"CPF: {self._cpf}")
        print(f"Idade: {self.idade}")
        print(f"IMC: {round(self.peso/(self.altura**2), 2)}") 
