from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca = None, qtdrodas = None, modelo = None, marchas = None, bagageiro = None):
        Veiculo.__init__(self, marca, qtdrodas, modelo)
        self.marchas = marchas
        self.bagageiro = bagageiro
    
    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        if (self.bagageiro):
            print(f'Número de Marchas: {self.marchas}\nBagageiro: Sim')
        else:
            print(f'Número de Marchas: {self.marchas}\nBagageiro: Não')