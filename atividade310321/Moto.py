from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca = None, qtdrodas = None, modelo = None, potencia = None, partidaEletrica = None):
        Automovel.__init__(self, marca, qtdrodas, modelo, potencia)
        self.partidaEletrica = partidaEletrica
    
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        if (self.partidaEletrica):
            print('Partida Elétrica: Sim')
        else:
            print('Partida Elétrica: Não')