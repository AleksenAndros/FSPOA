class Pessoa:

    def __init__(self, codigo, nome, endereco, telefone = None):
        self._codigo    = codigo
        self.nome       = nome
        self.__endereco = endereco
        self._telefone  = telefone

    def printName(self):
        print(f"Código:   {self._codigo}")
        print(f"Nome:     {self.nome}")
        print(f"Endereço: {self.__endereco}")
        print(f"Telefone: {self._telefone}")
