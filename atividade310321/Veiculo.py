class Veiculo():
    def __init__(self, marca = None, qtdrodas = None, modelo = None):
        self.marca = marca
        self.qtdrodas = qtdrodas
        self.modelo = modelo
        self.velocidade = 0
        
    def imprimirInformacoes(self):
        print(f'Marca: {self.marca}\nQuantidade de Rodas: {self.qtdrodas}\nModelo: {self.modelo}\nVelocidade: {self.velocidade}')

    def acelerar(self, valor):
        self.velocidade = self.velocidade + valor
        print(f'Velocidade atual: {self.velocidade}')

    def frear(self, valor):
        self.velocidade = self.velocidade - valor
        if(self.velocidade < 0):
            self.velocidade = 0
        print(f'Velocidade atual: {self.velocidade}')