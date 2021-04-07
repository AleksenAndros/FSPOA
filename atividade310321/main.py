'''
Crie o construtor para cada uma das classes

O método acelerar da classe Veículo deve somar o valor passado por parâmetro da velocidadeAtual do veículo.

O método frear da classe Veículo deve subtrair o valor passado por parâmetro da velocidadeAtual do veículo.

O método imprimirInformacoes de cada uma das classes deve exibir na tela o conteúdo de cada um dos atributos da classe.
'''

from Veiculo import Veiculo
from Automovel import Automovel
from Bicicleta import Bicicleta
from Moto import Moto
from Carro import Carro

tracado = '---------------------------'

veiculo = Veiculo('Toyota', 4, 'Corola')
veiculo.imprimirInformacoes()
print(tracado)

automovel = Automovel('Toyota', 4, 'Corola', 2.0)
automovel.imprimirInformacoes()
print(tracado)

moto = Moto('BMW', 2, '1300R', 1.3, True)
moto.imprimirInformacoes()
moto.acelerar(120)
print(tracado)

carrinho = Carro('Toyota', 4, 'Corola', 2.0, 4)
carrinho.imprimirInformacoes()
carrinho.acelerar(70)
carrinho.frear(40)
print(tracado)

bike = Bicicleta('Caloi', 2, 'CECI', 21, True)
bike.imprimirInformacoes()
bike.acelerar(40)
bike.frear(30)