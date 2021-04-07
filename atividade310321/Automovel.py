from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca = None, qtdrodas = None, modelo = None, potencia = None):
        Veiculo.__init__(self, marca, qtdrodas, modelo)
        self.potencia = potencia
        
    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f'Potência do motor: {self.potencia}')