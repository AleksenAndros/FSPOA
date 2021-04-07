from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca = None, qtdrodas = None, modelo = None, potencia = None, portas = None):
        Automovel.__init__(self, marca, qtdrodas, modelo, potencia)
        self.portas = portas
    
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print(f'Quantidade de Portas: {self.portas}')