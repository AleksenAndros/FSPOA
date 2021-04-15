from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

hr = '---------------------------------'

p1 = Pessoa(1, "Alexandre", "Rua dos Bobos, 0")
p1.printName()
print(hr)

f1 = Fisica(2, "Edson", "Avenida Tosco da Silva, 171", "111.111.111-11", 29, 85, 1.75, "3232-9898")
f1.imprimeCPF()
print(hr)

j1 = Juridica(3, "Nandocorp", "Via Mão, 111", "3266-1515", "123.456.789-1011/12", "1234567", 50)
j1.imprimeCNPJ()


